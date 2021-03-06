# def app(environ, start_response):
#     response_body = b"Hello World"
#     status = "200 ok"
#     start_response(status, headers=[])
#     return iter([response_body])

from api import API
from middleware import Middleware

app = API(templates_dir="templates", static_dir="static")


class SomeMiddleware(Middleware):
    def proces_request(self, req):
        print("Processing request", req.url)

    def proces_response(self, req, resp):
        print("Proeccsing response", req.url)
        pass


app.add_middleware(SomeMiddleware)


def custom_exception_handler(request, response, exception_cls):
    response.text = str(exception_cls)


app.add_exception_handler(custom_exception_handler)


@app.route("/home")
def home(request, response):
    response.text = "Hello from HOME page"


@app.route("/about", allowed_methods = ["get"])
def about(request, response):
    response.text = "Hello from ABOUT page"


@app.route("/hello/{name}")
def say_hello(request, response, name):
    response.text = f"Hello {name}"


@app.route("/sum/{num1}/{num2}")
def sum(request, response, num1, num2):
    total = int(num1) + int(num2)
    response.text = f"{num1} + {num2} = {total}"


@app.route("/book")
class BookResource:
    def get(self, req, resp):
        resp.text = "Books Page"

    def post(self, req, resp):
        resp.text = "Create books"


def handler(req, resp):
    resp.text = "YOLO"




@app.route("/template")
def template_handler(req, resp):
    resp.body = app.template(
        "index.html", context={"name": "academlo", "title": "Best framework", "author": "Nico"}
    ).encode()


@app.route("/template2")
def template_handler(req, resp):
    resp.html = app.template("index.html", context={"name": "Bumbo", "title": "Best Framework"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"name": "data", "type": "JSON"}


@app.route("/text")
def text_handler(req, resp):
    resp.text = "This is a simple text"