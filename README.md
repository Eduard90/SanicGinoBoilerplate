Boilerplate for Sanic+Gino ORM with CLI and async tests.

### Parts ###
 * Sanic - Async web framework
 * Gino - Async ORM
 * Alembic - PG migrations
 * Click - CLI
 * pytest - Tests
 * docker-compose - PG server and pgadmin4 in docker


### TODO ###
 * Add web handlers (+websocket)
 * Create pgadmin4 image
 
### DESCRIPTION ###

* You need start docker containers:
`docker-compose up -d`
* After run `pgadmin_perms_fix.sh` for fix permissions on `./volumes/pgadmin` directory.
`./pgadmin_perms_fix.sh`
* Install requirements:
`pip install -r requirements.txt`
* Set env variables in `.env` file (from `.env.example`)
* Apply DB migrations:
`./manage.py db migrate`
* Run `manage.py` script for CLI:
`./manage.py`
* ...
* ENJOY!