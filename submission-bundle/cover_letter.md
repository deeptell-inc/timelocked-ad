# Cover letter — Physical Review A (Regular Article)

**To:** The Editors, Physical Review A
**Manuscript:** "Does hiding the post-processing from a memory-limited eavesdropper raise the noise tolerance of QKD? Timelocked advantage distillation and the 20% barrier"
**Author:** Hikaru Wakaura, QIRI (Quantum Integrated Research Institute Inc.), Tokyo, Japan (h.wakaura@qiri.co.jp)
**Preprint:** arXiv:<<XXXX.XXXXX>> [quant-ph]

Dear Editors,

I submit the above manuscript for consideration as a Regular Article in Physical Review A.

The paper asks what a quantum computational timelock on the post-processing announcements can buy for decoy-state BB84 with advantage distillation, a question raised in this journal by Bae and Acín [Phys. Rev. A 75, 012334 (2007)], who noted that an eavesdropper forced to measure each probe before the parities are announced is held off until the 25% entanglement limit instead of the unconditional 20%. We separate the three announcements that a timelock can hide:

1. Hiding the parities buys nothing. We prove (Theorem 1, with an explicit measurement basis) that for every block size the best measurement made before the parities are announced attains the adaptive Helstrom value, so the eavesdropper's guessing probability is unchanged; the key length in the min-entropy accounting is then the collective-attack value, 17.66% at 10^14 pulses against the 17.30% certified by the entropic-uncertainty bound of Treplin, Kleinpaß and Orsucci, whose decoy-state statistics we reuse and whose four published thresholds our implementation reproduces to 0.1 percentage points.
2. Hiding the block partition is where the question of Bae and Acín lives. The protocol of Treplin et al. partitions the sifted key at random after the quantum phase, so an eavesdropper whose memory is shorter than the time between the probes of a block cannot bring them together. Under a stated assumption (feed-forward on unrelated probes and correlations across blocks are neglected) we model her by role-blind per-probe measurements; the Helstrom benchmark, which a numerical search over identical measurements does not improve at odd block sizes, then gives 20.8% (Shannon) and 20.7% (min-entropy) at b = 9 and 10^14 pulses, 19.4% and 20.6% in a post-selection sensitivity check, with 25% as asymptote. Semidefinite programmes with the partition as post-measurement information show that an adversary who holds up to six probes recovers most of the adaptive value, so at these sizes the gain rests on locality, and we state the remaining open question precisely.
3. Hiding the basis leaves the BB84 guessing probability unchanged at one- and two-bit blocks and, for the six-state protocol, shrinks the gain of the memoryless setting by an order of magnitude once two- or three-bit blocks are formed; the only timelock-dependent key-rate quantity that survives is a Shannon-accounting excess of 0.7 percentage points for block-local measurements.

Two by-products may be useful to practitioners: the key-length formula of Treplin et al. must be applied inside its stated domain phi_X + phi_Z < 1/2, outside of which an unconstrained optimiser certifies key at impossible error rates, and the Fano expression built from the majority-vote error underestimates a per-probe adversary's information in finite-key use.

Several recent proposals rely on encrypting or delaying the post-processing of QKD; this paper delimits what such a step can and cannot buy for qubit protocols, settles the parity announcement with a theorem, and reduces the partition announcement to a precisely stated open question. The main theorem is also a self-contained statement about state discrimination with post-measurement information that may interest readers outside QKD.

The manuscript has not been published and is not under consideration elsewhere. The code and data that produce every number are provided as Supplemental Material. I have no competing interests.

Suggested referees are listed on the submission form (see `suggested_referees.md`).

Sincerely,
Hikaru Wakaura
QIRI (Quantum Integrated Research Institute Inc.), 1-16-3 Akasaka, Minato-ku, Tokyo 107-0061, Japan
