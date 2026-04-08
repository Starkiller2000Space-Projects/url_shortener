# requirements

req:
	pip install -r requirements.txt

style-req:
	pip install -r requirements-style.txt

tests-req:
	pip install -r requirements-tests.txt

# run

run-local:
	uvicorn app.main:app --host 0.0.0.0 --port 8000

run:
	docker-compose up --build

stop:
	docker-compose down -v

# linting

lint:
	ruff check .
	mypy .

lint-fix:
	ruff format .
	ruff check --fix .
	mypy .

# formatting

test:
	pytest --cov=app . -v --cov-report term-missing --ignore=tests/test_api.py

test-full:
	pytest --cov=app . -v --cov-report term-missing
