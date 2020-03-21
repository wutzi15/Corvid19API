"""
WSGI config for the running of the app with gunicorn
"""
import sys
import os
from WebServer import app

if __name__ == '__main__':
    print("Running python")
    app.run(port=5000, debug=True)
