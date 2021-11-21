PROJECT_NAME = 'myskills'

# local
setup:
	pip install --upgrade pip
	pip install -r requirements.txt

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

# for local run
# step #1
dc up pg:
	docker-compose up pg
# step #2
run:
	python manage.py runserver


# docker
dc up:
	docker-compose up --build




# docker build --progress=plain . -t myskills