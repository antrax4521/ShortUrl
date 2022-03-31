# ShortUrl Project

## Core

ShortUrl core is build with:

- FastApi
- Python 3
- Postgresql
- Docker
- Docker-Compose
- Poetry
- Pytest


## Why FastApi?

FastApi is a powerfull Framework that allows develop fast and with less bugs, it uses Pydantic to validate the incoming making the develop process more easy and with less bugs.

The Shorturl Core was created thinking in the basics of microservices architecture based in the principle of single responsibility of the elements.


## Live Test & Documentation

You can see the service's documentation from your brower in the next url.

```
https://allgo.mx/docs
```


## Project setup

Copy env.example to .env

```
cp env.example .env
```

Once you have the .env you need to build the docker.
```
CURRENT_UID=$(id -u):$(id -u) docker-compose -f docker-compose-dev.yml build --build-arg user_id=$(id -u)
```

Then start the service.
```
CURRENT_UID=$(id -u):$(id -u) docker-compose -f docker-compose-dev.yml up
```

Finally run the migrations to create the models in the database.

First enter to the **dashboard container**
```
docker exec -it shorturl_backend_1 bash
```

And then run
```
alembic upgrade head
```
## Structure
The project's structure is the next

```
.
├── app
│   ├── alembic
│   │   ├── env.py
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       └── 536eb27ca285_url_model.py
│   ├── alembic.ini
│   ├── app
│   │   ├── api
│   │   │   ├── api_v1
│   │   │   │   ├── api.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── shorturl
│   │   │   │       ├── crud.py
│   │   │   │       ├── endpoints.py
│   │   │   │       ├── __init__.py
│   │   │   │       ├── tasks.py
│   │   │   │       ├── types.py
│   │   │   │       └── utils.py
│   │   │   ├── deps.py
│   │   │   └── __init__.py
│   │   ├── backend_pre_start.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   └── __init__.py
│   │   ├── db
│   │   │   ├── base_class.py
│   │   │   ├── base.py
│   │   │   ├── __init__.py
│   │   │   └── session.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── shortener.py
│   │   ├── service
│   │   ├── tests
│   │   │   ├── api
│   │   │   │   ├── api_v1
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── short_url.py
│   │   │   │   └── __init__.py
│   │   │   ├── conftest.py
│   │   │   ├── crud
│   │   │   │   ├── __init__.py
│   │   │   │   └── test_crud.py
│   │   │   └── __init__.py
│   │   ├── tests_pre_start.py
│   │   └── utils.py
│   ├── mypy.ini
│   ├── poetry.lock
│   ├── prestart.sh
│   ├── __pycache__
│   │   └── gunicorn_conf.cpython-37.pyc
│   ├── pyproject.toml
│   └── tests-start.sh
├── docker-compose-dev.yml
├── Dockerfile
├── env.example
└── README.md

```
## Run the Tests

To run the tests you need to enter to the container

```
docker exec -it shorturl_backend_1 bash
```

And then run the pytest commands.

```
pytest app/tests/api/api_v1/short_url.py <= Run the test making a request to the service.
pytest app/tests/crud/test_crud.py <= Persist to the database.
```

## Author

- Alfredo Gómez 

## Final words

Talk is cheap, show me the code! :)=
