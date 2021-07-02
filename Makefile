install:
	poetry install

bg:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

pkg-inst:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
