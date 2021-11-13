from wsgiref.simple_server import make_server
from framework.main import Framework
from application.routes import urls

# create an object for the WSGI application
application = Framework(urls)

with make_server('localhost', 8000, application) as httpd:
    print("Serving on port 8000...")

    httpd.serve_forever()
