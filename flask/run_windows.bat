@echo off
REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Run the Flask app
python app.py 