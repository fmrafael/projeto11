#!/bin/bash

NAME="mysite"

#path to your django application

DIR=/home/fmrafael/projeto10

USER=fmrafael

 

WORKERS=3

BIND=0.0.0.0:8002

#bind to port 8000

DJANGO_SETTINGS_MODULE=mysite.settings.settings

DJANGO_WSGI_MODULE=mysite.wsgi

LOG_LEVEL=error

cd $DIR

source /home/projeto10/venv/bin/activate

#activating the virtual environment

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

export PYTHONPATH=$DIR:$PYTHONPATH

exec /home/projeto10/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \

  --name $NAME \

  --workers $WORKERS \

  --user=$USER \


  --bind=$BIND \

  --log-level=$LOG_LEVEL \

  --log-file=-
