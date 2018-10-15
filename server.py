from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

TEMPLATE = \
"""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Euler drawing application</title>
  </head>
  <body>
    <h1>Hello [name]!!!!!</h1>
  </body>
</html>
"""


def hello_world(request):
    S = TEMPLATE.replace("[name]", request.matchdict["name"])
    return Response(S)

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello/{name}')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 9080, app)
    print("Serving....")
    server.serve_forever()

