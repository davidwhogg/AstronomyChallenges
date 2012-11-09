.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: pgm aps_prairie_2012-11-09.pdf

pgm:
	cd ../pgm ; make

%.pdf: %.tex ../pgm/*.pdf
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
