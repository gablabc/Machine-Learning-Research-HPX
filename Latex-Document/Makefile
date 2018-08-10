.phony: show all clean clean_all rebuild

all:
	latexmk -pdf document.tex

show: all
	xdg-open document.pdf

clean:
	latexmk -C

check:
	aspell check -l EN_us document.tex
