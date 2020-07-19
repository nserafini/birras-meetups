#! /usr/bin/env sh
set -e

export APP_MODULE="meetups.app:app"
export GUNICORN_CONF=/app/docker/api/gunicorn_conf.py

exec gunicorn -k uvicorn.workers.UvicornWorker -c "$GUNICORN_CONF" "$APP_MODULE"
