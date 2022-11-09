install:
	poetry install

test:
	poetry run pytest -s

coverage:
	poetry run pytest --cov=pipe --cov-report=term --cov-report=xml tests/

lint:
	poetry run flake8
