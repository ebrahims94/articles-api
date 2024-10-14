#!/bin/bash

# Apply migrations
python manage.py migrate

# run tests
python manage.py test --pattern="*_test.py"

# Start Django development server
python manage.py runserver 0.0.0.0:8000