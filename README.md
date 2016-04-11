This repository provides an example of how to install Open North's [Open511](http://open511.org/) server and client software.

## Installation

### Install prerequisites

* Python 2.7, with pip, virtualenv, and lxml
* PostgreSQL 9.x, with PostGIS

If you're running Ubuntu, the corresponding package names are `python-pip python-virtualenv python-lxml postgresql-9.1-postgis`. Note that Ubuntu's packaged version of PostGIS is quite old -- you may be better off installing packages from the [Postgres apt repository](https://wiki.postgresql.org/wiki/Apt).

### Create a database

You need a Postgres database. If you're using PostGIS 2.x, this is quite simple:

```
$ createdb open511example
$ psql open511example -c "CREATE EXTENSION postgis;"
```

If you're using an earlier version of PostGIS, there are a few more steps; the [GeoDjango documentation](https://docs.djangoproject.com/en/1.6/ref/contrib/gis/install/#installation) has details.

### Create a Python virtualenv

A "virtualenv" is the standard Python way to manage dependencies: you create a lightweight Python "environment" and install packages locally to that environment. You don't _need_ to do this: you can install all Python dependencies globally (which probably means running several of the commands below as root). But a virtualenv is definitely the preferred way of deploying Python software.

To create: `$ virtualenv open511example`

That'll create a directory containing your new environment. To enable it, run `source open511example/bin/activate`. When the environment is enabled, you'll see `(open511example)` before your shell prompt. Remember to enable it before running any `pip` or `python` command for Open511.

### Install Python dependencies

```(open511example)$ pip install -r requirements.txt```

### Initialize the database

You'll likely need to edit `open511_example/settings.py` to enter your database
connection info. Then, run:

```(open511example)$ python manage.py migrate```

The first time you run this, it'll ask you to create a user. You should.

### Load sample data

```
(open511example)$ python manage.py loaddata sample_data/jurisdiction.json
Installed 2 object(s) from 1 fixture(s)
(open511example)$ python manage.py open511_import sample_data/events.xml 
2 entries imported
```

### Launch the app

```(open511example)$ python manage.py runserver```

Then visit http://localhost:8000/ in your browser.

### Install the map UI

Open North has created a user interface for viewing and editing events on an Open511 server. (For production use, note that it's licensed under the AGPL.)

To install it, make sure that you have [Node.JS](http://nodejs.org/) (0.10 or greater) installed. (You also need NPM, the Node package manager; this is generally included with Node, but some distributions may need you to install a separate `npm` package.)

Then run ```(open511example)$ pip install -e git+http://github.com/open511/roadcast.git#egg=roadcast```

If everything goes well, you should be able to start the server (as above) and visit http://localhost:8000/map/

### Set up data imports

The usual way to load data feeds into the system is via `open511_import` run as a scheduled task. For example, to load updates from a TMDD feed, run the following commands every time a TMDD message is received:

```
(open511example)$ open511-convert tmdd.xml -f xml > converted-tmdd.xml
(open511example)$ python manage.py open511_import converted-tmdd.xml
```
