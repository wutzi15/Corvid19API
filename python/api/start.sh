#!/bin/bash
cd /app
#python WebServer.py

gunicorn -b '127.0.0.1:5000' wsgi:app --threads 4 --certfile /certs/cert.pem --keyfile /certs/privkey.pem