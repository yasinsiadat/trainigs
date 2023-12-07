import requests

def detect_framework(port):
    url = f"http://localhost:{port}"

    try:
        response = requests.get(url)
        headers = response.headers

        # Check for specific headers that indicate the framework
        if 'uvicorn' in headers.get('server', '').lower():
            return "FastAPI"
        elif 'werkzeug' in headers.get('server', '').lower():
            return "Flask"
        elif 'wsgiserver' in headers.get('server', '').lower():
            return "Django"
        else:
            return "Unknown"

    except requests.exceptions.RequestException as e:
        return f"Error connecting to {url}: {e}"

if __name__ == "__main__":
    ports = [8001, 8002, 8003]

    for port in ports:
        framework = detect_framework(port)
        print(f"Port {port}: {framework}")
