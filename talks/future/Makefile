.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: hogg_simons_2015-09-18.pdf

%.pdf: %.tex hogg_presentation.tex
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
