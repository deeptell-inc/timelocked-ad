"""Six-state, b=3 mixed-basis blocks, bases+parities hidden: achievable success (rank-1 projective, 64 outcomes),
vectorised alternating ascent. Lower bound on P_joint; compare with P_ad."""
import sys, os, itertools, math, numpy as np, time
sys.path.insert(0, os.path.dirname(__file__))
from hidden_basis_sdp import block_states, parity, helstrom
def problem(c_psi, b):
    thetas = list(itertools.product("ZXY", repeat=b)); states, D = block_states(c_psi, 0.0, b, thetas)
    classes = [(th, c) for th in thetas for c in itertools.product((0,1), repeat=b-1)]
    R0=[]; R1=[]
    for (th,c) in classes:
        a0=[a for (t,a) in states if t==th and parity(a)==c and a[0]==0][0]; a1=[a for (t,a) in states if t==th and parity(a)==c and a[0]==1][0]
        R0.append(states[(th,a0)]); R1.append(states[(th,a1)])
    R0=np.array(R0); R1=np.array(R1); prior=1.0/(len(thetas)*2**b)
    pad=sum(helstrom(r0,r1) for r0,r1 in zip(R0,R1))/len(classes)
    return R0,R1,prior,pad,D
def value(W,R0,R1,prior):
    L0=np.real(np.einsum('yi,cij,yj->yc',W.conj(),R0,W)); L1=np.real(np.einsum('yi,cij,yj->yc',W.conj(),R1,W))
    return prior*np.sum(np.maximum(L0,L1)), (L0>=L1)
def ascend(R0,R1,prior,dim,seed,outer=30,inner=150):
    rng=np.random.default_rng(seed); W,_=np.linalg.qr(rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))); W=W.T  # rows = outcome vectors
    v,dec=value(W,R0,R1,prior)
    for _ in range(outer):
        G=prior*(np.einsum('yc,cij->yij',dec,R0)+np.einsum('yc,cij->yij',~dec,R1))   # (y,dim,dim)
        def f(W_): return np.real(np.einsum('yi,yij,yj->',W_.conj(),G,W_))
        eta=0.5; cur=f(W)
        for _ in range(inner):
            Gam=2*np.einsum('yij,yj->yi',G,W)   # d f / d W^*  (rows)
            A=W@Gam.conj().T                    # (y,y)
            grad=Gam-(A+A.conj().T)@W/2
            while True:
                Q,_=np.linalg.qr((W+eta*grad).T); Wn=Q.T; fn=f(Wn)
                if fn>=cur: break
                eta*=0.5
                if eta<1e-13: break
            if eta<1e-13: break
            W,cur=Wn,fn; eta=min(eta*1.5,5.0)
        vn,dec=value(W,R0,R1,prior)
        if vn-v<1e-12: v=vn; break
        v=vn
    return v
if __name__=="__main__":
    b=int(sys.argv[1])
    for c_psi in (0.8,0.65):
        t0=time.time(); R0,R1,prior,pad,D=problem(c_psi,b); dim=R0.shape[1]; best=0
        for s in range(3):
            v=ascend(R0,R1,prior,dim,s); best=max(best,v); print(f"  b={b} c_psi={c_psi} seed {s}: {v:.6f}  ({time.time()-t0:.0f}s)",flush=True)
        print(f"six-state b={b} mixed, bases+parities hidden: c_psi={c_psi} D={D:.3f}  P_achievable>={best:.6f}  P_ad={pad:.6f}  err_ratio<={(1-best)/(1-pad):.4f}",flush=True)
