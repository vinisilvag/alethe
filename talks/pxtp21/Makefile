.PHONY: clean pngslides all

all:
	latexmk -shell-escape -pdflatex=lualatex -pdf talk

pngslides:
	mkdir -p pngslides
	pdftocairo talk.pdf pngslides/talk -png -transp -scale-to-x 1920 -scale-to-y 1080
