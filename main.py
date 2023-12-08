from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

app = FastAPI()

# Disable default exception handler to make error responses less predictable
@app.exception_handler(HTTPException)
async def custom_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(content={"detail": "Server Error"}, status_code=500)

# Remove Server header to make the server signature less obvious
@app.middleware("http")
async def remove_server_header(request: Request, call_next):
    response = await call_next(request)
    response.headers.pop("server", None)
    return response

# Add custom headers to responses to introduce noise
@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Custom Value"
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8002, log_level="info", access_log=False)
