# intership
For the intership project 
this project for create the same export from three differnet frameworks are Django and Flask and Fastapi 
at first you should install them using this commands :

Django: pip install Django
Flask: pip install Flask
FastAPI: pip install fastapi uvicorn

and for run ] one of the framework you can use special commands :
Flask:
1-python app.py

FastAPI:
1-uvicorn main:app --reload

Django:
1-cd myproject
2-python manage.py runserver

and if you want to run on specific port run this commands :

Flask:
1-export FLASK_RUN_PORT=8000
2-flask run
(if its not worked run this "pip install Flask")

FastAPI:
1-uvicorn main:app --reload --port 8000

Django:
1-cd myproject
2-python manage.py runserver 8000


