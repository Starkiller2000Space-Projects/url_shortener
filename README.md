# URL Shortener Service

[![CI](https://github.com/Starkiller2000Space-Projects/url-shortener/actions/workflows/ci.yml/badge.svg)](https://github.com/Starkiller2000Space-Projects/url-shortener/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![License](https://img.shields.io/badge/license-MIT-blue)

URL shortening service (similar to [bitly](https://bitly.com/)) implemented with [**FastAPI**](https://fastapi.tiangolo.com/) + [**PostgreSQL**](https://www.postgresql.org/).  
Supports redirect via short ID, click counting, and statistics.

## Requirements

- Python 3.14
- Docker (for containerized run)
- PostgreSQL (when running locally without Docker)

## Running the Project

### 1. Clone the repository
```bash
git clone https://github.com/Starkiller2000Space-Projects/url_shortener.git
cd url_shortener
```

### 2. Environment setup

Copy the [example configuration](./.env.example) and edit it, then place it as `.env` file.

### 3. Run with Docker Compose (recommended)

Build and run using docker-compose:

```bash
make run
```

After startup:
- API: `http://localhost:8000`
- Documentation: `http://localhost:8000/docs`
- Interactive ReDoc: `http://localhost:8000/redoc`

Stop:

```bash
make stop
```

### 4. Run locally

Install dependencies for local development / execution:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac or venv\Scripts\activate (Windows)
make req
make run-local
```

## Run linting

```bash
make style-req
make lint      # only lint
make lint-fix  # lint and fix
```

## Run tests

```bash
make tests-req
make test       # without api testing
make test-full  # with api testing using test-client
```

Expected result: all tests pass, coverage 100%.

## License

[MIT License](./LICENSE)

## Technologies

| Component     | Technology                           |
|---------------|--------------------------------------|
| Framework     | FastAPI 0.104.1                      |
| ORM           | SQLAlchemy 2.0                       |
| Database      | PostgreSQL 15 (SQLite for tests)     |

## Authors

- :white_check_mark: [Starkiller2000Space](https://gitlab.com/Starkiller2000Space)