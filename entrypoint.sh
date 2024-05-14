#!/bin/sh

echo "Export settings"
export DJANGO_SETTINGS_MODULE=sber_testovoe.settings.docker

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Starting server"
python manage.py runserver 0.0.0.0:8003