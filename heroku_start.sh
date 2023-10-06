#!/bin/sh

# Install sentence-transformers without dependencies
pip3 install --no-deps sentence-transformers

# Start the application
gunicorn app:app --timeout 25 --log-level info --graceful-timeout 30
