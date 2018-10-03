#!/bin/bash

NAME="mvp2-demo"
NUM_WORKERS=4

echo "Starting ${NAME}"

# Start your gunicorn
gunicorn -b 0.0.0.0:8002 --name ${NAME} --workers ${NUM_WORKERS} grunserver:app
# gunicorn -w 4 -b 0.0.0.0:8002 runserver:app