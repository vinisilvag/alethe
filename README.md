The Proof Format -- Speculative Specification
=============================================

This repository hosts a specification of the proof format used by veriT
right now.  It will also soon be available on CVC5.

Right now the specification is speculative: rather than being cast
in stone, it will improve as solvers, proof reconstructions, and
tools develop.  Our approach is pragmatic.  We refine the format
and especially the rules as we gather experience.

## Building the Specifications

The specification are in the folder `spec`.  The main source file is the
`doc.tex` file. You can use `make` in the `spec` directory to compile
the document.

Syntax highlighting uses the `pygments` tool.  Hence, this tool must
be installed.  Furthermore, Latex must be compiled with shell escaping
allowed.  To do this the argument `-shell-escape` must be given to the
Latex command. `latexmk` also accepts this argument and hands it to Latex.

The continuous integration pipeline also builds the document. Hence,
the pdf is available in the artifact browser of the CI pipelines.
