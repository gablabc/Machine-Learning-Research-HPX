.phony: show all clean clean_all rebuild

all:
	latexmk -pdf document.tex

show: all
	xdg-open document.pdf

clean:
	latexmk -C

check:
	aspell check -l EN_us document.tex
	aspell check -l EN_us Sections/Introduction.tex
	aspell check -l EN_us Sections/Math_Notation.tex
	aspell check -l EN_us Sections/Data_generation.tex
	aspell check -l EN_us Sections/Data_analysis.tex
	aspell check -l EN_us Sections/Machine_Learning.tex
