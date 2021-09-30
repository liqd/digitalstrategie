# digitalstrategie

[![Coverage Status](https://coveralls.io/repos/github/liqd/digitalstrategie/badge.svg?branch=main)](https://coveralls.io/github/liqd/digitalstrategie?branch=main)

Welcome to digitalstrategie

## How to run

Install dependencies
```
$ make install
```

### Start a local server:
```
$ make watch
```
### Create superuser:
```
$ source venv/bin/activate  # to start the virtual env
$ python manage.py createsuperuser
```
and fill in the following prompts
```
$ Username (leave blank to use '...'):
$ Email address:
$ Password:
$ Password (again):
```

or do:
```
$ make fixtures
```
This will add an user with name `admin` and PW `password`.

Login with credentials at http://localhost:8006/admin/
