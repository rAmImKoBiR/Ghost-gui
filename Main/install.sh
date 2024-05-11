#!/bin/bash

# Install python, pip, and required dependencies
pkg install -y python python-dev clang openssl-dev libcrypt-dev libffi-dev make

# Install Flask using Pip
pip install flask

# Download and install ADB
pkg install -y android-tools

echo "Installation completed successfully."
