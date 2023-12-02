from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def my_route():
    return "Hello from Yasin!"
