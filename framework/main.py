class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    """ base class of WSGI-framework """

    def __init__(self, routes: dict):
        self.routes = routes

    def __call__(self, environ: dict, start_response):
        # get URL address
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # select view
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        # run view
        code, body = view()
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
