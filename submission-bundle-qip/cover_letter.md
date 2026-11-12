# Cover letter — Quantum Information Processing (Regular Article)

**To:** The Editor-in-Chief, Quantum Information Processing
**Manuscript:** "Parity-independent optimal eavesdropping on advantage distillation in quantum key distribution"
**Author:** Hikaru Wakaura, QIRI (Quantum Integrated Research Institute Inc.), Tokyo, Japan (h.wakaura@qiri.co.jp)
**Preprint:** Research Square, https://doi.org/10.21203/rs.3.rs-11453979/v1 (posted 22 October 2026, CC BY 4.0, under the title "Does hiding the post-processing from a memory-limited eavesdropper raise the noise tolerance of QKD? Timelocked advantage distillation and the 20% barrier")

Dear Editor,

I submit the above manuscript for consideration as a Regular Article in Quantum Information Processing.

The main result is a theorem on quantum state discrimination with post-measurement information. In repetition-code advantage distillation the eavesdropper's probes for an accepted block are in one of two product states determined by the announced parity, and the optimal (Helstrom) measurement differs from one parity class to the next. Theorem 1 shows that for every block size these Helstrom measurements are compatible: one projective measurement, given explicitly as the orbit of a single Helstrom pair under Pauli operators, attains the Helstrom success probability in all parity classes at once, and the parity is needed only to read the outcome. The proof is short and self-contained (Appendix A); the construction agrees with a semidefinite programme for blocks of up to four bits and is reproduced numerically to 10^-14 for blocks of up to nine bits.

The theorem sharpens a remark of Bae and Acín [Phys. Rev. A 75, 012334 (2007)], who noted that an eavesdropper who must measure each probe before the parities are announced is held off until the 25% entanglement limit instead of 20%. It shows that early measurement alone costs her nothing, so delaying or encrypting the parity announcement, as several recent proposals for timelocked or encrypted post-processing do, cannot lift the 20% limit. The manuscript then works out the consequences for decoy-state BB84:

1. In the min-entropy accounting the finite-key threshold is the collective-attack value, 17.66% at 10^14 pulses, against the 17.30% certified by the entropic-uncertainty bound of Treplin, Kleinpaß and Orsucci, whose decoy-state statistics are reused and whose four published thresholds the implementation reproduces to 0.1 percentage points.
2. The 25% limit rests on the block partition, not on the parity: the eavesdropper must be unable to bring the probes of a block together. Under a stated per-probe model the threshold is 20.7–20.8% at nine-bit blocks and 10^14 pulses; semidefinite programmes with the partition as post-measurement information show that a memory holding up to six probes recovers most of the adaptive value, and the remaining open question is stated precisely.
3. Hiding the basis leaves the BB84 guessing probability unchanged at one- and two-bit blocks and, for the six-state protocol, shrinks the gain of the memoryless setting by an order of magnitude once blocks are formed.

The manuscript has not been published and is not under consideration elsewhere. The code and data that produce every number are publicly available (reference [Wak26] of the manuscript, https://github.com/deeptell-inc/timelocked-ad) and attached as Online Resource 1. I have no competing interests. Suggested reviewers are given on the submission form.

Sincerely,
Hikaru Wakaura
QIRI (Quantum Integrated Research Institute Inc.), 1-16-3 Akasaka, Minato-ku, Tokyo 107-0061, Japan
