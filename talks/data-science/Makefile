.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: hogg_picscie_2014-05-16.pdf

%.pdf: %.tex
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
