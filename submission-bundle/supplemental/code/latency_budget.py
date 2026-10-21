"""P5 / C4: (i) AD-stage arithmetic cost relative to LDPC reconciliation,
(ii) announcement-delay budget tau_ann vs quantum-memory coherence t_coh and
computational timelock t_comp. Pure arithmetic, deterministic.
Output: data/latency_budget.csv"""
import os, csv

# (i) per raw-key bit operations. LDPC belief propagation: ~ iters * (row weight) * ops/check;
# published FPGA engines (Walenta 2014 / Constantin 2017: 4 Mbps distilled on Virtex-6) bound
# the reconciliation throughput; AD adds (b-1) XOR + 1 compare per block of b bits, i.e. < 1 XOR/bit.
ldpc_ops_per_bit = 25 * 6 * 4          # 25 iterations x dv=6 x ~4 ops (check+variable update), order of magnitude
rows = []
for b in (2, 3, 5, 9, 15):
    ad_ops_per_bit = (b - 1 + 1) / b   # XORs + compare, per raw bit
    rows.append(dict(kind="ad_cost", b=b, ad_ops_per_bit=ad_ops_per_bit,
                     ldpc_ops_per_bit=ldpc_ops_per_bit, ratio=ad_ops_per_bit / ldpc_ops_per_bit))

# (ii) delay budget. Messages that must stay hidden until Eve's memory has decohered:
#   V-A: AD parities c_A, c_B + IR syndrome;  V-B: also basis announcements.
# Requirement (A2): Delta_m > t_coh - (t_m - t_rx). With immediate processing t_m ~ t_rx,
# so Delta_m > t_coh. Option (i) plain delay tau_ann = Delta_m (adds latency tau_ann to key
# delivery); option (ii) encryption: Delta_m = t_comp - t_m, no added latency, needs PQC key.
for t_coh in (1e-3, 1e-1, 1.0, 10.0, 100.0):
    for t_comp_years in (1, 10):
        t_comp = t_comp_years * 365.25 * 86400
        rows.append(dict(kind="delay_budget", t_coh_s=t_coh, t_comp_s=t_comp,
                         tau_ann_plain_s=t_coh, latency_added_plain_s=t_coh,
                         latency_added_encrypted_s=0.0, margin_ratio=t_comp / t_coh))
out = os.path.join(os.path.dirname(__file__), "..", "..", "data", "latency_budget.csv")
keys = sorted({k for r in rows for k in r})
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=keys); w.writeheader(); w.writerows(rows)
for r in rows:
    print(r)
print("wrote", out)
