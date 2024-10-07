nix:
	SOURCE_DATE_EPOCH=$(date +%s) latexmk -pdf -pvc -interaction=nonstopmode -shell-escape -lualatex doc

doc:
	latexmk -pdf -shell-escape -lualatex -synctex=1 doc

nonstop:
	latexmk -interaction=nonstopmode -pdf -shell-escape -lualatex doc
