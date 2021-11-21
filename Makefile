PROJECT_NAME = 'myskills'

# target: makemigrations — make migrations for the database
makemigrations:
	pipenv run ./app/manage.py makemigrations

# target: migrate — migrate the database
migrate:
	pipenv run ./app/manage.py migrate

# target: run — run project with local environment
run:
	pipenv run ./app/manage.py runserver






# docker build --progress=plain . -t myskills