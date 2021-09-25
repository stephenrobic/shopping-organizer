#!/bin/sh

#stop the execution of script if a command or pipeline has an error
set -e

pg_ctlcluster 9.6 master stop -- -m smart

echo "Waiting for postgres .."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done
echo "PostgreSQL started"

python manage.py migrate --noinput
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py runserver 0.0.0.0:8000
