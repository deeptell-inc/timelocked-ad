"""Build paper/main.tex from manuscript.md (revtex4-2). Run from the project root: python3 paper/md2tex.py"""
import re, os
md=open('manuscript.md').read()
body=md[md.find('# Does hiding'):]
title=body.splitlines()[0][2:]
secs=re.split(r'\n## ', body)
S={}
for sec in secs[1:]:
    head, _, txt = sec.partition('\n'); S[head.strip()]=txt.strip()
abstract=S['Abstract']; refs=S['References']
order=[k for k in S if k not in ('Abstract','References')]
labels={"3. The adversary's information on a distilled bit":'sec:eve','5. Numerical results':'sec:num','7. Discussion':'sec:disc','4. Finite-key secure key length':'sec:key'}
def cites(t):
    t=re.sub(r'Refs\. \[([^\]]+)\]', lambda m: 'Refs.~\\cite{'+m.group(1).replace(' ','')+'}', t)
    t=re.sub(r'Ref\. \[([^\]]+)\]', lambda m: 'Ref.~\\cite{'+m.group(1).replace(' ','')+'}', t)
    t=re.sub(r'\[([A-Za-z]+\d+(?:, ?[A-Za-z]+\d+)*)\]', lambda m: '\\cite{'+m.group(1).replace(' ','')+'}', t)
    return t
def conv(t):
    t=re.sub(r'`([^`]+)`', lambda m: '\\texttt{'+m.group(1).replace('_','\\_')+'}', t)
    t=t.replace('\\%','%').replace('%','\\%').replace('−','-').replace('–','--').replace('—','---').replace('“','``').replace('”',"''").replace('’',"'")
    t=cites(t)
    for a,b in [('Appendix C.1','Appendix~\\ref{app:C}.1'),('Appendix C.2','Appendix~\\ref{app:C}.2'),('Appendix C.3','Appendix~\\ref{app:C}.3'),('Appendix C.4','Appendix~\\ref{app:C}.4'),('Appendix C.5','Appendix~\\ref{app:C}.5'),('Appendix A','Appendix~\\ref{app:A}'),('Appendix B','Appendix~\\ref{app:B}'),('Appendix C','Appendix~\\ref{app:C}'),('Theorem 1','Theorem~1'),('Lemma 1','Lemma~1'),('Lemma 2','Lemma~2'),('Table 1','Table~\\ref{tab:thr}'),('Table 2','Table~\\ref{tab:sdp}'),('Table 3','Table~\\ref{tab:ps}'),('Table 4','Table~\\ref{tab:hp}'),('Figure 2','Fig.~\\ref{fig:eve}'),('Figure 4','Fig.~\\ref{fig:thr}'),
                ('Section 3','Sec.~\\ref{sec:eve}'),('Section 4','Sec.~\\ref{sec:key}'),('Section 5','Sec.~\\ref{sec:num}'),('Section 7','Sec.~\\ref{sec:disc}'),
                ('Protocol 1','Protocol~1'),('Proposition 1','Proposition~1'),('Theorem 9','Theorem~9'),('Eq. (','Eq.~('),('Eqs. (','Eqs.~('),
                ('Appendix B','Appendix~B'),('Conjecture 1','Conjecture~1'),('e.g. ','e.g.\\ '),('i.e. ','i.e.\\ '),('i.i.d. ','i.i.d.\\ '),('et al.','\\emph{et al.}')]:
        t=t.replace(a,b)
    t=re.sub(r'^\*\*(.+?)\*\*', r'\\paragraph*{\1}', t, flags=re.M)
    t=re.sub(r'\*\*(.+?)\*\*', r'\\emph{\1}', t)
    t=re.sub(r'(?<![\*\w])\*(?!\*)([^*\n]+?)\*(?!\*)', r'\\emph{\1}', t)
    t=re.sub(r'"([^"]+)"', r"``\1''", t)
    return t
def displays(t, labels):
    out=[]; k=0
    parts=re.split(r'\$\$(.+?)\$\$', t, flags=re.S)
    for i,p in enumerate(parts):
        if i%2==0: out.append(p); continue
        eq=p.strip()
        if 'U|\\!\\uparrow' in eq:
            a,b=eq.split(',\\qquad '); out.append('\n\\begin{align}\n'+a+',\\\\\n'+b+'\n\\end{align}\n'); continue
        lab=labels[k] if k<len(labels) else ''; k+=1
        L=('\\label{%s}'%lab) if lab else ''
        if 'J_b(\\delta)=' in eq:
            a,b=eq.split(',\\qquad '); out.append('\n\\begin{align}\n'+a.replace('=','&=',1)+','+L+'\\\\\n'+b.replace('=','&=',1)+'\\nonumber\n\\end{align}\n')
        elif 'P^{\\rm joint}_b=\\max' in eq:
            a,b=eq.split(',\\qquad ',1); b=b.replace(',\\quad ',',\\ \\ ').replace('\\sum_f M_f','\\textstyle\\sum_f M_f')
            out.append('\n\\begin{align}\n'+a.replace('=','&=',1)+','+L+'\\\\\n&\\quad '+b+'\\nonumber\n\\end{align}\n')
        elif '\\ell_{\\rm QCT}' in eq:
            a,b=eq.split('-\\Delta_{\\rm AEP}'); b1,b2=b.split('-4\\log_2')
            out.append('\n\\begin{align}\n'+a.replace('\\le','&\\le',1)+L+'\\\\\n&\\quad-\\Delta_{\\rm AEP}'+b1+'\\nonumber\\\\\n&\\quad-4\\log_2'+b2+'\\nonumber\n\\end{align}\n')
        elif ',\\qquad ' in eq:
            a,b=eq.split(',\\qquad ',1)
            out.append('\n\\begin{align}\n'+a.replace('=','&=',1)+','+L+'\\\\\n&\\quad '+b+'\\nonumber\n\\end{align}\n')
        else:
            out.append('\n\\begin{equation}\n'+eq+L+'\n\\end{equation}\n')
    return ''.join(out)
def table(txt, label, caption, colspec, star=False):
    lines=[l for l in txt.splitlines() if l.startswith('|')]
    rows=[[c.strip() for c in l.strip('|').split('|')] for l in lines if not set(l.replace('|','').strip())<=set('-: ')]
    body='\\\\\n'.join(' & '.join(c.replace('\\%','%').replace('%','\\%') for c in r) for r in rows[1:])
    head=' & '.join(rows[0]); env='table*' if star else 'table'
    return '\\begin{%s}[t]\\centering\\caption{%s}\\label{%s}\n\\begin{tabular}{%s}\\toprule\n%s\\\\\\midrule\n%s\\\\\\bottomrule\\end{tabular}\\end{%s}\n'%(env,caption,label,colspec,head,body,env)
tex=[r'''\documentclass[aps,pra,twocolumn,superscriptaddress,nofootinbib]{revtex4-2}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,graphicx,booktabs,hyperref}
\graphicspath{{figures/}}
\begin{document}
\title{'''+conv(title)+r'''}
\author{Hikaru Wakaura}
\email{h.wakaura@qiri.co.jp}
\affiliation{QIRI (Quantum Integrated Research Institute Inc.),
1--16--3 Akasaka, Minato-ku, Tokyo 107--0061, Japan}
\date{\today}
\begin{abstract}
'''+conv(abstract)+r'''
\end{abstract}
\maketitle
''']
for k in order:
    name=k.split('. ',1)[1]; lab=labels.get(k)
    if k.startswith('Appendix'):
        if '\\appendix' not in ''.join(tex): tex.append('\\appendix\n')
        name=k.split('. ',1)[1]
        tex.append('\\section{%s}\\label{app:%s}\n'%(name, k[9]))
        tex.append(conv(S[k])+'\n'); continue
    tex.append('\\section{%s}%s\n'%(name, ('\\label{%s}'%lab) if lab else ''))
    txt=S[k]
    if k.startswith('5.'):
        paras=txt.split('\n\n'); labels5=['tab:thr','tab:sdp','tab:ps','tab:hp']; ti=0; n=0
        while n < len(paras):
            p=paras[n]
            if p.startswith('|'):
                cap=paras[n+1][paras[n+1].find('. ')+2:] if n+1 < len(paras) and paras[n+1].startswith('Table ') else ''
                ncol=len([c_ for c_ in p.splitlines()[0].strip('|').split('|')])
                tex.append(table(p, labels5[ti], conv(cap), 'l'*ncol, star=(ncol>=6))); ti+=1; n+=(2 if cap else 1); continue
            tex.append(conv(p)+'\n\n'); n+=1
        tex.append(r'''\begin{figure*}[t]\centering\includegraphics[width=0.95\textwidth]{fig3_rate_vs_qber.pdf}
\caption{Secure key rate $\ell/N$ versus QBER for $N=10^8$ (left) and $N=10^{14}$ (right): BB84 one-way (Ref.~\cite{T25}, Eq.~(94)), AD (Ref.~\cite{T25}, Eq.~(93)) and the Helstrom per-probe benchmark (class H, under the assumptions of A4; not a guarantee against class W) in both entropy accountings, for $b=1,3,5,9$.}\label{fig:rates}\end{figure*}
\begin{figure}[t]\centering\includegraphics[width=\columnwidth]{fig4_threshold_vs_b.pdf}
\caption{Threshold QBER versus block size $b$: finite-key values at $N=10^{14}$ for Ref.~\cite{T25}, the Helstrom per-probe benchmark (class H, all $b$) and the joint model, and the asymptotic single-photon thresholds (60-digit arithmetic); horizontal lines at 20\% and 25\%.}\label{fig:thr}\end{figure}
''')
        continue
    txt=conv(txt)
    if k.startswith('3.'):
        txt=displays(txt,['eq:IEind','eq:sdp'])
        txt+=r'''

\begin{figure}[t]\centering\includegraphics[width=\columnwidth]{fig2_eve_info.pdf}
\caption{Adversary's uncertainty per distilled bit, $1-I_E$, versus QBER for block sizes $b=1,3,5,9,15$: Helstrom per-probe benchmark, class H (solid, Eq.~\eqref{eq:IEind} with tally decoding), joint block measurement (dash-dotted, adaptive Helstrom value), and the entropic-uncertainty term of Ref.~\cite{T25} (dashed, same colour). Vertical lines: 20\% and 25\%.}\label{fig:eve}\end{figure}
'''
    else:
        txt=displays(txt,['eq:ell'] if k.startswith('4.') else [])
    tex.append(txt+'\n')
tex.append('\\begin{thebibliography}{99}\n')
for line in refs.splitlines():
    m=re.match(r'- \[([A-Za-z0-9]+)\] (.*)', line)
    if m: tex.append('\\bibitem{%s} %s\n'%(m.group(1), m.group(2).replace('\\%','%').replace('%','\\%')))
tex.append('\\end{thebibliography}\n\\end{document}\n')
out=''.join(tex).replace('https://github.com/deeptell-inc/timelocked-ad','\\url{https://github.com/deeptell-inc/timelocked-ad}')
open(os.path.join(os.path.dirname(__file__) or '.','main.tex'),'w').write(out)
print("main.tex written")
