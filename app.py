from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_route():
    return "Hello from Yasin!"

if __name__ == '__main__':
    app.run(debug=False)
