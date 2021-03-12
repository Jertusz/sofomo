# sofomo
Recruitment task  
To properly run the project poetry is highly recommended. Instructions
on how to do it are available at the bottom of README.

## Endpoint list  
    account/register/ - register user
    account/login/ - login user
    api/ip/ - all ip related endpoints
    api/url/ - all url related endpoints

## Used packages
requests - connection to external api  
djangorestframework - used to provide basic behaviour to all REST stuff  
flake8 - code formatting
isort - autoformatting imports
black - reformatting code (fixing line breaks, quotes)
gunicorn - used to reduce strain on server  
psycopg2 - used because of postgres db being used by app  
python-decouple - separation of sensitive info, easier split between dev and prod env


### Example .env 

    DJANGO_KEY=nb-=b1lif_low2c#w&!ly9($u68k$oamnv7u2mpu5!0%tmv+5)
    DEBUG=False
    DB_NAME=sofomo
    DB_TEST_NAME=sofomo_test
    DB_USER=sofomo
    DB_PASSWORD=sofomo_postgres
    DB_PORT=5430
    DB_HOST=127.0.0.1
    
## Update tables in a database

`python manage.py migrate`

## Run development server

`python manage.py runserver`

## Build and run dockerized server

`docker-compose up --build`

## Code quality

`flake8` - check stylistics  
`black .` - reformat all  
`isort .` - sort import accordingly to the project's rules

# Poetry

[Install the tool](https://python-poetry.org/docs/#installation)  
[Install the dependencies](https://python-poetry.org/docs/cli/#install)  
[Set env](https://python-poetry.org/docs/managing-environments/#switching-between-environments)  
[Run inside env](https://python-poetry.org/docs/cli/#run)  
[Build](https://python-poetry.org/docs/cli/#build)  
[Update](https://python-poetry.org/docs/cli/#update)
