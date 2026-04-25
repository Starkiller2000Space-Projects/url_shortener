# requirements

req:
	uv sync

req-dev:
	uv sync --extra lint,test

# run

run-local:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

run:
	docker-compose up --build

stop:
	docker-compose down -v

# linting

lint:
	uv run ruff check .
	uv run mypy .

lint-fix:
	uv run ruff format .
	uv run ruff check --fix .
	uv run mypy .

# formatting

test:
	uv run pytest --cov=app . -v --cov-report term-missing --ignore=tests/test_api.py

test-full:
	uv run pytest --cov=app . -v --cov-report term-missing
