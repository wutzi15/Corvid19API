#!/bin/bash
cd /app
python WebServer.py

#gunicorn -b '127.0.0.1:8000' wsgi:app --threads 4