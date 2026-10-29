# Cover letter — Journal of Physics A: Mathematical and Theoretical (Paper)

**To:** The Editors, Journal of Physics A: Mathematical and Theoretical
**Manuscript:** "Timelocked advantage distillation and the 20% barrier of quantum key distribution"
**Author:** Hikaru Wakaura, QIRI (Quantum Integrated Research Institute Inc.), Tokyo, Japan (h.wakaura@qiri.co.jp)
**Preprint:** Research Square, https://doi.org/10.21203/rs.3.rs-11453979/v1 (posted 22 October 2026, CC BY 4.0, under an earlier title)

Dear Editors,

I submit the above manuscript for consideration as a Paper in Journal of Physics A: Mathematical and Theoretical, section Quantum Information and Computation.

The paper determines what a quantum computational timelock on the post-processing announcements can buy for decoy-state BB84 with advantage distillation. Bae and Acín noted that an eavesdropper forced to measure each probe before the distillation parities are announced is held off until the 25% entanglement limit instead of the unconditional 20%, and Bocquet, Alléaume and Leverrier [J. Phys. A 45, 025305 (2012)] computed in this journal what a memoryless eavesdropper costs BB84 and six-state QKD without distillation. We combine the two settings and separate the three announcements that a timelock can hide:

1. Hiding the parities buys nothing. We prove (Theorem 1, with an explicit measurement basis) that for every block size the best measurement made before the parities are announced attains the adaptive Helstrom value, so the eavesdropper's guessing probability is unchanged; the key length in the min-entropy accounting is then the collective-attack value, 17.66% at 10^14 pulses against the 17.30% certified by the entropic-uncertainty bound of Treplin, Kleinpaß and Orsucci, whose decoy-state statistics we reuse and whose four published thresholds our implementation reproduces to 0.1 percentage points.
2. Hiding the block partition is where the remark of Bae and Acín lives. The protocol partitions the sifted key at random after the quantum phase, so an eavesdropper whose memory is shorter than the time between the probes of a block cannot bring them together. Under a stated assumption we model her by role-blind per-probe measurements; the Helstrom benchmark, which a numerical search over identical measurements does not improve at odd block sizes, then gives 20.8% (Shannon) and 20.7% (min-entropy) at b = 9 and 10^14 pulses, with 25% as asymptote. Semidefinite programmes with the partition as post-measurement information show that an adversary who holds up to six probes recovers most of the adaptive value, so at these sizes the gain rests on locality, and we state the remaining open question precisely.
3. Hiding the basis leaves the BB84 guessing probability unchanged at one- and two-bit blocks and, for the six-state protocol, shrinks the gain of the memoryless setting by an order of magnitude once two- or three-bit blocks are formed.

The main theorem is a self-contained result on state discrimination with post-measurement information: for the product-state families that arise from repetition-code distillation, the Helstrom measurements of all parity classes are simultaneously realisable by one Pauli-orbit basis. Two by-products concern implementations of the finite-key formula of Treplin et al.: its domain phi_X + phi_Z < 1/2 must be enforced, and the Fano expression built from the majority-vote error underestimates a per-probe adversary's information.

The manuscript has not been published and is not under consideration elsewhere. The code and data that produce every number are publicly available in a citable repository (reference [Wak26] of the manuscript, https://github.com/deeptell-inc/timelocked-ad). I have no competing interests. Suggested referees are listed in `suggested_referees.md`.

Sincerely,
Hikaru Wakaura
QIRI (Quantum Integrated Research Institute Inc.), 1-16-3 Akasaka, Minato-ku, Tokyo 107-0061, Japan
