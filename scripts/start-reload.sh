#! /usr/bin/env sh
set -e

export APP_MODULE="meetups.app:app"
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-5000}
LOG_LEVEL=$(echo ${LOG_LEVEL:-info} | tr '[:upper:]' '[:lower:]' )

exec uvicorn --reload --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"
