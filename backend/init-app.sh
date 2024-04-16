#!/bin/bash
python manage.py migrate
python manage.py load_init_data
python manage.py make_ml_model
python manage.py runserver 0.0.0.0:8000
