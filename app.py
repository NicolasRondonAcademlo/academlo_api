
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


def say_hello(request, response, persona_name):
    response.text = f"Hello {persona_name}"

