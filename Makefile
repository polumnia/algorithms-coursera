init: clean init-poetry

init-poetry:
	poetry env remove 3.7 || true
	poetry install

clean:  ## delete files defined in .gitignore
	git clean -Xdf

pylint:
	poetry run pylint slice_sem_plaintext_extractor

flake8:
	poetry run flake8

mypy:
	poetry run mypy slice_sem_plaintext_extractor tests

lint: flake8 pylint mypy

test:
	poetry run pytest
