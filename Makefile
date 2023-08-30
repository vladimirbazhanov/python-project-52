dev:
	poetry run ./manage.py runserver

install:
	poetry install

start:
	poetry run gunicorn task_manager.wsgi:application
