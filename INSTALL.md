## Installation

The installation requires certain software to be installed in your machine

## Requirements

- [Python](https://www.python.org/)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper)

## Steps

* Clone the project

```
git clone https://github.com/ciudadanointeligente/deldichoalhecho.git
```

* Create a virtualenv and enter the directory

```
mkvirtualenv deldichoalhecho
cd deldichoalhecho
```

* Install the project requirements

```
pip install -r requirements.txt
```

* Crate database

```
python manage.py syncdb
```

* Install migrations

```
python manage.py migrate
```

* Run server

```
python manage.py runserver
```

And now you can access at [http://localhost:8000](http://localhost:8000)

## Deploy to Heroku

This app can be deployed to [heroku](http://heroku.com) to do so you need to create an account and install the [heroku toolbelt](https://toolbelt.heroku.com/), then you need to create an app and relate a database for it (for example [heroku postgres](https://postgres.heroku.com) which has a free layer).

Then you can publish your project by doing 

```
git push heroku master
```

After that you need to sync the database by doing


```
heroku run ./manage.py syncdb
```

And run the migrations


```
heroku run ./manage.py migrate
```
