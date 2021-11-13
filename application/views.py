""" Module containing web application controllers — views """


class Index:
    def __call__(self):
        return '200 OK', 'OK (WSGI app is working)'
