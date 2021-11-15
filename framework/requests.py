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
