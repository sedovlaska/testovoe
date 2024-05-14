#!/bin/sh

echo "Waiting for chrome..."
while ! nc -z chrome 4444; do
  sleep 0.1
done
echo "Chrome started"

echo "Waiting for Django..."
while ! nc -z django 8003; do
  sleep 0.1
done
echo "Django started"

echo "Export settings"
export DJANGO_SETTINGS_MODULE=sber_testovoe.settings.docker

echo "Starting Tests"
if [ "$1" ]
then
  echo "Only $1 Tests"
  pytest -m "$1"
else
  pytest
fi