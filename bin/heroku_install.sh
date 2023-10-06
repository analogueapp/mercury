#!/bin/sh

# Install main dependencies
pip3 install -r requirements.txt

pip3 install http://download.pytorch.org/whl/cpu/torch-2.1.0%2Bcpu-cp311-cp311-linux_x86_64.whl

# Install no-deps requirements
pip3 install --no-deps sentence-transformers