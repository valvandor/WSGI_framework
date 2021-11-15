# Processing a GET request with parameters
class GetRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        """
        Parse an input string containing request params into a dict
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ: dict) -> dict:
        """
        Returns a dict of request parameters
        """
        # get query params as a string
        query_string = environ['QUERY_STRING']

        return GetRequests.parse_input_data(query_string)


# Processing a POST request with params
class PostRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        """
        Parse an input string containing request params into a dict
        """
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

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
        """
        Decodes input string of bytes and
        converted it to dict via function parse_input_data
        """
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
