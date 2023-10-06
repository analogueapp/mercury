#!/bin/sh

pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu

pip3 install -r requirements.txt

pip3 install --no-deps sentence-transformers