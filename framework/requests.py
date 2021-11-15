class ParseMixin:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        """ Parse an input string containing request params into a dict """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result


class GetRequests(ParseMixin):
    """ Class for processing a GET request with parameters """
    @staticmethod
    def get_request_params(environ: dict) -> dict:
        """ Finds query params as a string from environ and converts it to dict """
        # get query params as a string
        query_string = environ['QUERY_STRING']
        request_params = GetRequests.parse_input_data(query_string)
        return request_params


class PostRequests(ParseMixin):
    """ Class for processing a POST request with parameters """
    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        """
        Reads file-like object environ['wsgi.input'] depending on the length of the content passed in the request
        If content is empty, returns an empty string of bytes
        Else returns read string of bytes from object environ['wsgi.input']
        """
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        """ Decodes input string of bytes and converts it to dict """
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        """ Returns a dict with query params """
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
