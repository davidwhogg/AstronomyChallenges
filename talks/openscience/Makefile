.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: hogg_aas_223_code_sharing.pdf

%.pdf: %.tex
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
