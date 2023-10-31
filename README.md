# Gemeinsam Digital: Berlin

## How to run

#### Install dependencies
```
$ make install
```

#### Start a local server:
```
$ make watch
```

Start local server with elastic search:

Open two terminal windows.
1. Start elastic search in the first one:
```
$ sudo docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" -e "logger.level=DEBUG" -e 'xpack.security.enabled=false' -e 'xpack.security.enrollment.enabled=false' docker.elastic.co/elasticsearch/elasticsearch:8.10.2
```

2. Run the server in the second one. But before you do that, update the search index.
```
$ source venv/bin/activate  # to start the virtual env
$ python manage.py update_index
$ make watch
```

#### Create superuser:
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
