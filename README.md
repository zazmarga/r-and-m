# Rick and Morty

### Requirements:

1. Endpoint, which return random character from the World of Rick and Morty series.
2. Endpoint get `search_string` as an argument and return list of all characters who contains the  `search_string` in the name.
3. On regular basis, app downloads data from external service to inner DB.
4. Requests of implemented Api should work with local DB (Take data from DB, not from Rick & Morty Api).


### Technologies to use:

1. Public Api: https://rickandmortyapi.com/documentation
2. Use Celery as task scheduler for data synchronization for Rich & Morty Api.
3. Python, Django/Flask/FastAPI, ORM, PostgreSQL, Git.
4. All endpoints should be documented via Swagger.


### How to run:

* Create venv: `python -m venv venv`
* Activate it: `venv/Scripts/activate`
* Install requirements: `pip install -r requirements.txt`
* Create new Postgres DB & user (using docker postgres-image)
    1)  `docker pull postgres`
    2)  `docker run --name rick_and_morty -e POSTGRES_PASSWORD=<password db> -d postgres`
    3)  `docker exec -it rick_and_morty psql -U postgres`
    4) postgres:  `\c rick_and_morty`
    5) postgres:  `CREATE DATABASE rick_and_morty;`
    6) postgres:  `CREATE USER rick_and_morty_user WITH ENCRYPTED PASSWORD 'password db';`
    7) postgres:  `GRANT ALL PRIVILEGES ON DATABASE rick_and_morty TO rick_and_morty_user;`
    8) postgres:  `\l`  (for check DB)
* Run migrations: `python manage.py migrate`
* Run Redis Server: `docker run -d -p 6379:6379 redis`
* Run Celery worker for tasks handing: `celery -A rick_and_morty_api worker -l INFO`
<or `celery -A rick_and_morty_api worker --pool=solo -l INFO` (me)>
* Run Celery beat for tasks scheduling: `celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`
* Create schedule for running sync in DB
* Run app: `python manage.py runserver`
