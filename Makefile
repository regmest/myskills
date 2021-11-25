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
dcup_pg:
	docker-compose up pg
# step #2
run:
	python manage.py runserver


# docker
dcup:
	docker-compose up --build


# coverage check
coverage:
	coverage run manage.py test
	coverage report -m

coverage_submit:
	COVERALLS_REPO_TOKEN=$COVERALLS_REPO_TOKEN coveralls



# docker build --progress=plain . -t myskills