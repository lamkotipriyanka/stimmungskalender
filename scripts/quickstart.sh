#!/usr/bin/env bash

# Use the developer settings for a quick start
cp .env.sample .env
# Create a virtualenv that holds all dependencies
python3 -m venv virtualenv
# We don't need postgres support for now, so let's comment it out
sed -i 's/psycopg2/#psycopg2/' requirements/common.txt
# Install the developer dependencies
./virtualenv/bin/pip install -r requirements/dev.txt
# Initialize the sqlite database
./virtualenv/bin/python manage.py migrate
# Create the frontend texts
./virtualenv/bin/django-admin compilemessages
# Create a user account
./virtualenv/bin/python manage.py createsuperuser
# Start the app
./virtualenv/bin/python manage.py runserver
