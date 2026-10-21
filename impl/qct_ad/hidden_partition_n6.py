import sys, os, time, csv
sys.path.insert(0, os.path.dirname(__file__))
from hidden_partition_sdp import run
rows=[]
for D in (0.10, 0.20):
    t0=time.time(); pj,pad,pind,c,nf = run(6, 2, D, solver="SCS")
    rows.append(dict(n=6,b=2,D=D,c_psi=c,P_ind=pind,P_joint_hidden_partition=pj,P_adaptive=pad,n_povm=nf)); print(rows[-1], "%.0fs"%(time.time()-t0), flush=True)
with open(os.path.join(os.path.dirname(__file__),"..","..","data","hidden_partition_n6.csv"),"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print("done")
