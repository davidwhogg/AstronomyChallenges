.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: pgm astroinformatics_2012-09-11.pdf

pgm:
	cd ../pgm ; make

%.pdf: %.tex *.jpg *.png
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
