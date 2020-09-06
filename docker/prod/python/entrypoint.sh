#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compress

echo "Running command '$*'"
exec /bin/bash -c "$*"
