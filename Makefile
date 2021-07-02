install:
	poetry install

bg:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

pkg-install:
	python3 -m pip install --user dist/*.whl

