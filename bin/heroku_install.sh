#!/bin/sh

# Install main dependencies
pip3 install -r requirements.txt

# Install no-deps requirements
pip3 install --no-deps sentence-transformers