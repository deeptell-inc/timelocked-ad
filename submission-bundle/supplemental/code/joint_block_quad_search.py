"""Search: m_{(0,y')} = X^{yt} D_q (u0+v0)/sqrt2, m_{(1,y')} = G m_{(0,y')}, q quadratic form on {0,1}^b (per y').
Greedy over y' with backtracking; accept q if orthogonal to all accepted vectors. Then check P_free = P_ad."""
import numpy as np, itertools, math, sys, time
def setup(b, D):
    c = 3 - 2/(1-D); th = 0.5*math.acos(c); cs, sn = math.cos(th), math.sin(th)
    X = list(itertools.product((0,1), repeat=b)); dim = 2**b; Xa = np.array(X)
    alpha = np.array([cs**(b-sum(x))*sn**sum(x) for x in X])
    ev = (Xa.sum(1)%2==0)
    u0 = alpha*ev; u0/=np.linalg.norm(u0); v0 = alpha*(~ev); v0/=np.linalg.norm(v0)
    g = (u0+v0)/math.sqrt(2)
    Gsign = np.where(ev, 1.0, -1.0)
    # quadratic forms: monomials z_i (b) and z_i z_j (i<j)
    mons = [Xa[:,i] for i in range(b)] + [Xa[:,i]*Xa[:,j] for i in range(b) for j in range(i+1,b)]
    Mon = np.array(mons)                       # (nmon, dim) 0/1
    nmon = len(mons)
    Q = np.array(list(itertools.product((0,1), repeat=nmon)))   # all quadratic forms (2^nmon, nmon)
    Sgn = np.where((Q @ Mon) % 2 == 0, 1.0, -1.0)                # (nq, dim) sign vectors
    return X, Xa, dim, alpha, g, Gsign, Sgn, Q, c
def xflip_perm(Xa, t):
    idx = {tuple(x):i for i,x in enumerate(Xa)}
    return np.array([idx[tuple((x+t)%2)] for x in Xa])
def run(b, D, verbose=True):
    X, Xa, dim, alpha, g, Gsign, Sgn, Q, c = setup(b, D)
    yps = list(itertools.product((0,1), repeat=b-1))
    cands = []    # per y': array of candidate m0 vectors (nq, dim)
    for yp in yps:
        yt = np.array(((1+sum(yp))%2,)+yp)
        perm = xflip_perm(Xa, yt)             # (X^yt v)(x) = v(x xor yt)
        base = Sgn * g[None,:]                # D_q g
        cands.append(base[:, perm])           # X^yt D_q g
    accepted = []; choice = []
    def ok(m0):
        m1 = Gsign*m0
        if abs(m0@m1) > 1e-9: return False
        for a in accepted:
            if abs(a@m0) > 1e-9 or abs(a@m1) > 1e-9: return False
        return True
    t0=time.time()
    def bt(k):
        if k == len(yps): return True
        C = cands[k]
        if accepted:
            A = np.array(accepted); dots = np.abs(C @ A.T).max(1)
            mask = dots < 1e-9
        else:
            mask = np.ones(len(C), bool)
        mask &= np.abs(np.sum(C*(Gsign*C), axis=1)) < 1e-9
        for qi in np.nonzero(mask)[0]:
            accepted.append(C[qi]); accepted.append(Gsign*C[qi]); choice.append(qi)
            if bt(k+1): return True
            accepted.pop(); accepted.pop(); choice.pop()
        return False
    found = bt(0)
    if not found: print(f"b={b} D={D}: no solution in quadratic family"); return None
    M = np.array(accepted)
    # P_free
    P = 0.0
    for cc in yps:
        a0 = np.array((0,)+cc); a1 = 1-a0
        s0 = np.where((Xa@a0)%2==0,1.0,-1.0)*alpha; s1 = np.where((Xa@a1)%2==0,1.0,-1.0)*alpha
        P += np.sum(np.maximum((M@s0)**2, (M@s1)**2))
    P/=dim; pad = 0.5+0.5*math.sqrt(1-c**(2*b))
    print(f"b={b} D={D}: found in {time.time()-t0:.1f}s; orth err {np.linalg.norm(M@M.T-np.eye(dim)):.1e}; P_free={P:.12f} P_ad={pad:.12f} gap={pad-P:.1e}")
    if verbose:
        for yp, qi in zip(yps, choice): print("   y'=",yp," q=",Q[qi])
    return M, choice, Q
if __name__ == "__main__":
    for b in [int(x) for x in sys.argv[1:]]:
        run(b, 0.2, verbose=(b<=4))
