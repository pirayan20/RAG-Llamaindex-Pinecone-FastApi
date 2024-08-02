#!/bin/sh

set -e
. .venv/bin/activate
exec uvicorn app.main:app --host 0.0.0.0 --port 8080
