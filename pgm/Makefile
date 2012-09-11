.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: abc.pdf wl.pdf gaia.pdf

%.pdf: %.tex
	latex $*
	dvipdf $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
