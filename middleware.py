from webob import Request


class Middleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.app.handle_request(request)
        return response(environ, start_response)

    def add_middleware(self, middleware_cls):
        self.app = middleware_cls(self.app)

    def proces_request(self, req):
        pass

    def proces_response(self,req, resp):
        pass

    def handle_request(self, request):
        self.proces_request(request)
        response = self.app.handle_request(request)
        self.proces_response(request,response)
        return response
