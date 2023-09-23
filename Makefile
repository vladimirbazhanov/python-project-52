dev:
	poetry run ./manage.py runserver

migrations:
	poetry run ./manage.py migrate

install:
	poetry install

start:
	poetry run gunicorn task_manager.wsgi:application

lint:
	poetry run flake8 --exclude=migrations

tests:
	poetry run ./manage.py test

