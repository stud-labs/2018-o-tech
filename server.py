from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
import os.path

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

TDIR = os.getcwd()


def t(template):
    return os.path.join(TDIR, "templates", template)


def hello_world(request):
    return {"name": request.matchdict["name"]}


def calc(request):
    print(request.POST)
    return "Ok"


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello/{name}')
        config.add_view(hello_world,
                        route_name='hello',
                        renderer=t('index.pt'))
        config.include('pyramid_chameleon')
        config.add_static_view(name='vendors', path=t('vendors'))
        config.add_static_view(name='build', path=t('build'))

        config.add_route('calc', '/calc')
        config.add_view(calc, route_name='calc')

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Serving....")
    server.serve_forever()
