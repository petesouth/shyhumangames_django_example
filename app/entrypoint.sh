#!/bin/bash
# Start cron in the background
cron

# Start Django application
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
