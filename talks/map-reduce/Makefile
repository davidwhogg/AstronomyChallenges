.SUFFIXES: .tex .pdf
RM = /bin/rm -fv
PDFLATEX = pdflatex

all: pgm hogg-zoom-4-slide-small-017.jpg aps_prairie_2012-11-09.pdf

hogg-zoom-4-slide-small-017.jpg:
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-000.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-001.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-002.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-003.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-004.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-005.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-006.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-007.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-008.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-009.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-010.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-011.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-012.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-013.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-014.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-015.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-016.jpg
	curl -O http://cosmo.nyu.edu/hogg/research/2010/08/15/hogg-zoom-4-slide-small-017.jpg

pgm:
	cd ../../pgm ; make

%.pdf: %.tex ../../pgm/*.pdf
	$(PDFLATEX) $*

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
