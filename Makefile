dev:
	poetry run ./manage.py runserver

migrate:
	poetry run ./manage.py migrate

install:
	poetry install

start:
	poetry run gunicorn task_manager.wsgi:application

lint:
	poetry run flake8

tests: migrate
	poetry run ./manage.py test

tests-with-coverage:
	poetry run coverage run ./manage.py test

