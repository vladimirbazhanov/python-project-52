dev:
	poetry run ./manage.py runserver

migrations:
	poetry run python ./manage.py migrate

install:
	poetry install

start:
	poetry run gunicorn task_manager.wsgi:application
