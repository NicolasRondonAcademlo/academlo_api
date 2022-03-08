
# def app(environ, start_response):
#     response_body = b"Hello World"
#     status = "200 ok"
#     start_response(status, headers=[])
#     return iter([response_body])

from api import API
app = API()

@app.route("/home")
def home(request, response):
    response.text = "Hello from HOME page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from ABOUT page"


@app.route("/hello/{name}")
def say_hello(request, response, name):
    response.text = f"Hello {name}"


@app.route("/sum/{num1}/{num2}")
def sum(request, response, num1, num2):
    total = int(num1) + int(num2)
    response.text = f"{num1} + {num2} = {total}"
