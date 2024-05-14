#!/bin/sh

#echo "Waiting for chrome..."
#while ! nc -z chrome 4444; do
#  sleep 0.1
#done
#echo "Chrome started"
#
#echo "Waiting for firefox..."
#while ! nc -z firefox 4444; do
#  sleep 0.1
#done
#echo "Firefox started"
#
#echo "Waiting for Edge..."
#while ! nc -z chrome 4444; do
#  sleep 0.1
#done
#echo "Edge started"

echo "Waiting for Django..."
while ! nc -z django 8003; do
  sleep 0.1
done
echo "Django started"

echo "Waiting for selenium-hub..."
while ! nc -z selenium-hub 4444; do
  sleep 0.1
done
echo "selenium-hub started"


echo "Export settings"
export DJANGO_SETTINGS_MODULE=sber_testovoe.settings.docker

pytest -m ui -n 2