install:
	poetry install

start:
	poetry run gunicorn task_manager.wsgi:application
