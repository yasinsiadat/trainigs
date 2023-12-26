def post_request(worker, req, environ, resp):
    resp.headers.pop('server', None)
