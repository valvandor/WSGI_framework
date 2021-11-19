from quopri import decodestring as quopri_decodestring

from framework.requests import GetRequests, PostRequests


class PageNotFound404:
    def __call__(self):
        return '404 WHAT', '404 PAGE Not Found'


class Framework:

    """ base class of WSGI-framework """

    def __init__(self, routes: dict):
        self.routes = routes

    def __call__(self, environ: dict, start_response):
        # show environment variables by order in console
        # print(*sorted((f'{key}: {value}' for key, value in environ.items())), sep='\n')

        # get URL address
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # create object of request as a dict
        request = {}

        # get request method
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params
            print(f'GET-parameters: {request_params}')

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
            print(f'POST-data: {Framework.decode_value(data)}')
        
        # select view
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        # run view
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data: dict):
        """
        Converts the transmitted data in accordance with UTF-8
        """
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri_decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
