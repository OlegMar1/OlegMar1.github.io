#!/bin/bash
# To make this script executable, run: chmod +x run_linux.sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the Flask app
python app.py 