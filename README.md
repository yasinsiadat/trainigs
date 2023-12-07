# Internship Project

This project is aimed at creating the same export using three different frameworks: Django, Flask, and FastAPI.

## Installation

To set up the project, install the required frameworks using the following commands:

- Django: `pip install Django`
- Flask: `pip install Flask`
- FastAPI: `pip install fastapi uvicorn`

## Running the Frameworks

After installation, you can run each framework using the following commands:

### Flask

```bash
python3 app.py```

###  FastAPI Flask
```bash
uvicorn main:app --reload

###Django
```bash
cd myproject
python3 manage.py runserver

###Running on Specific Ports
If you want to run on a specific port, use the following commands:

Flask
```bash

export FLASK_RUN_PORT=8000
flask run
# If it doesn't work, run: pip install Flask

###FastAPI
```bash

uvicorn main:app --reload --port 8000

###Django
```bash

cd myproject
python3 manage.py runserver 8000
