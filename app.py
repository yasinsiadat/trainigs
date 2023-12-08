from flask import Flask, request
import os

app = Flask(__name__)

# Remove default error handler to make error responses less predictable
@app.errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500

# Remove Server header to make the server signature less obvious
@app.after_request
def remove_server_header(response):
    response.headers.pop("server", None)
    return response

# Add custom headers to responses to introduce noise
@app.after_request
def add_custom_headers(response):
    response.headers["X-Custom-Header"] = "Custom Value"
    return response

if __name__ == '__main__':
    # Use an environment variable for the port to make it less predictable
    port = int(os.environ.get("FLASK_PORT", 8001))
    app.run(port=port, debug=False)
