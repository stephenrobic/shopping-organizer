#!/bin/sh

#stop the execution of script if a command or pipeline has an error
set -e

echo "Waiting for postgres .."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "PostgreSQL started"

python manage.py migrate --noinput
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
