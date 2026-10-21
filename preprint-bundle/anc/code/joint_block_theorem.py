"""Explicit construction (Theorem 1): basis {P_{y'} g_+^{(0)}, P_{y'} g_-^{(0)}}, P_{y'} = X^{yt(y')} Z^{(0, L y')},
yt(y') = (1+|y'| mod 2, y'), L = prefix-XOR on Z_2^{b-1}. Decision: outcome (y', s) -> guess a1 = 0 iff s = (-1)^{y'.(Ly' xor c)}.
Checks: orthonormality, E_c g_+^{(c)} = g_+^{(c)}, E_c g_-^{(c)} = 0, and total success = P_ad, for b = 2..9."""
import numpy as np, itertools, math, sys
def check(b, D):
    c = 3 - 2/(1-D); th = 0.5*math.acos(c); cs, sn = math.cos(th), math.sin(th)
    Xa = np.array(list(itertools.product((0,1), repeat=b))); dim = 2**b
    alpha = np.array([cs**(b-x.sum())*sn**x.sum() for x in Xa])
    ev = (Xa.sum(1)%2==0); Gs = np.where(ev,1.0,-1.0)
    u0 = alpha*ev; u0/=np.linalg.norm(u0); v0 = alpha*(~ev); v0/=np.linalg.norm(v0)
    gp = (u0+v0)/math.sqrt(2); gm = (u0-v0)/math.sqrt(2)
    idx = {tuple(x):i for i,x in enumerate(Xa)}
    def Z(s): return np.where((Xa@np.array(s))%2==0,1.0,-1.0)
    def Xperm(t): return np.array([idx[tuple((x+np.array(t))%2)] for x in Xa])
    yps = list(itertools.product((0,1), repeat=b-1))
    rows=[]; meta=[]
    for yp in yps:
        yt = ((1+sum(yp))%2,)+yp
        L = tuple(int(sum(yp[:j+1])%2) for j in range(b-1))      # prefix xor
        zsgn = Z((0,)+L); perm = Xperm(yt)
        for s in (+1,-1):
            g = gp if s>0 else gm
            rows.append((zsgn*g)[perm]); meta.append((yp,L,s))
    M = np.array(rows); orth = np.linalg.norm(M@M.T-np.eye(dim))
    worst_proj=0.0; P=0.0
    for cc in yps:
        Qc = Z((0,)+cc); gpc = Qc*gp; gmc = Qc*gm
        sel = np.array([ s == (1 if (sum(a*b_ for a,b_ in zip(yp,[(l+cv)%2 for l,cv in zip(L,cc)]))%2==0) else -1) for (yp,L,s) in meta])
        Ec = M[sel].T@M[sel]
        worst_proj = max(worst_proj, np.linalg.norm(Ec@gpc-gpc), np.linalg.norm(Ec@gmc))
        a0 = np.array((0,)+cc); psi0 = Z(a0)*alpha; psi1 = Z(1-a0)*alpha
        P += 0.5*(psi0@Ec@psi0 + psi1@(np.eye(dim)-Ec)@psi1)
    P/=len(yps); pad = 0.5+0.5*math.sqrt(1-c**(2*b))
    return orth, worst_proj, P, pad
for b in range(2,10):
    for D in (0.05, 0.15, 0.24):
        o,w,P,pad = check(b,D)
        print(f"b={b} D={D}: orth {o:.1e}  Helstrom-cond {w:.1e}  P={P:.15f} P_ad={pad:.15f} diff={abs(P-pad):.1e}", flush=True)
