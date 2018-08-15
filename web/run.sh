#!/usr/bin/env bash
python3 manage.py makemigrations
python3 manage.py migrate
uwsgi --ini /usr/src/app/web/uwsgi.ini
tail -f /usr/src/app/logs/uwsgi.log