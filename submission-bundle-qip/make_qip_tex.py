"""Build submission-bundle-qip/main.tex from paper/main.tex (run paper/md2tex.py first).
Run from the project root: python3 submission-bundle-qip/make_qip_tex.py
Changes: single-column 12 pt, keywords, wide tables squeezed, and a "Statements and Declarations"
section (required by Quantum Information Processing) that absorbs the data availability paragraph."""
import os, re
FUNDING = ""   # author to set, e.g. "No funding was received for conducting this study."
AI_USE = ""    # author to set if a statement on the use of AI tools is to be included
KEYWORDS = "Quantum key distribution, Advantage distillation, State discrimination, Post-measurement information, Helstrom measurement"
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, "..", "paper", "main.tex")).read()
def sub(old, new, count=1):
    global t
    assert t.count(old) >= 1, old
    t = t.replace(old, new) if count == 0 else t.replace(old, new, count)
sub(r"\documentclass[aps,pra,twocolumn,superscriptaddress,nofootinbib]{revtex4-2}",
    r"\documentclass[aps,pra,preprint,12pt,showkeys,superscriptaddress,nofootinbib]{revtex4-2}")
sub("\\end{abstract}\n", "\\end{abstract}\n\\keywords{" + KEYWORDS + "}\n")
sub(r"\begin{table*}[t]\centering", r"\squeezetable\begin{table*}[t]\centering", 0)
m = re.search(r"\\paragraph\*\{Data availability\.\} (.*)\n", t)
decl = ["\\section*{Statements and Declarations}",
        "\\paragraph*{Competing interests.} The author has no competing interests to declare that are relevant to the content of this article.",
        "\\paragraph*{Data availability.} " + m.group(1) + " The same material is provided as Online Resource 1.",
        "\\paragraph*{Author contributions.} The author is the sole contributor to this work."]
if FUNDING: decl.insert(2, "\\paragraph*{Funding.} " + FUNDING)
if AI_USE: decl.append("\\paragraph*{Use of AI tools.} " + AI_USE)
t = t[:m.start()] + "\n\n".join(decl) + "\n" + t[m.end():]
open(os.path.join(here, "main.tex"), "w").write(t)
print("submission-bundle-qip/main.tex written; funding statement:", "set" if FUNDING else "NOT SET", "; AI-use statement:", "set" if AI_USE else "NOT SET")
