from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
import euler
import io

TDIR = os.getcwd()
FIGURE = '/var/tmp/figure.svg'


def t(template):
    return os.path.join(TDIR, "templates", template)


def hello_world(request):
    return {"name": 'User'}


def calc(request):
    # MultiDict([('T0', '100'), ('tend', '60'), ('h', '0.01'), ('k', '0.1')])
    d = request.POST

    vars = 'T0 tend Tenv h k'.split(" ")
    types = [int, int, int, float, float]

    par = {}
    for var, t in zip(vars, types):
        par[var] = t(d[var])

    # euler.simple_euler(T0=par['T0'],
    #                    Tenv=par['Tenv'],
    #                    h=par['h'],
    #                    tend=par['tend'],
    #                    k=par['k'])

    result = euler.simple_euler(**par)

    par['result'] = result
    par['name'] = 'User'

    plt.figure(figsize=[4, 3])
    plt.plot(result)
    # plt.axis('off')
    # plt.gca().set_position([0, 0, 1, 1])

    plt.savefig(FIGURE)   # TODO: Try to save in memory

    i = open(FIGURE, "r")
    svg = i.read()
    i.close()

    svg = '<svg'+svg.split('<svg')[1]

    par['svg'] = svg

    return par


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('form', '/')
        config.add_view(hello_world,
                        route_name='form',
                        renderer=t('index.pt'))
        config.include('pyramid_chameleon')
        config.add_static_view(name='vendors', path=t('vendors'))
        config.add_static_view(name='build', path=t('build'))

        config.add_route('calc', '/calc')
        config.add_view(calc,
                        route_name='calc',
                        renderer=t('calc.pt'))

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    print("Serving....")
    server.serve_forever()
