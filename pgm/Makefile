.SUFFIXES: .py .pdf
RM = /bin/rm -fv

all: bca.pdf weaklensing.pdf gaia.pdf mapreduce.pdf crowded.pdf

%.pdf: %.py
	python $*.py

clean:
	$(RM) *.log *.aux *.dvi *.bbl *.blg
