import requests

from blablacarapi.debug import Debug
from blablacarapi.api_exceptions import BlaBlaCarRequestApiException


__author__ = 'ivan.arar@gmail.com'


def bind_request(**request_data):

    class ApiRequest(object):

        model = request_data.get('model')
        api_path = request_data.get('api_path')
        method = request_data.get('method', 'GET')
        query_parameters = request_data.get('query_parameters')

        def __init__(self, client, debug, *path_params, **query_params):
            client.request = self
            self.debug = debug
            self.client = client
            self.parameters = {'query': {}, 'path': []}
            self._set_parameters(*path_params, **query_params)

        def _set_parameters(self, *path_params, **query_params):
            """
            Prepares the list of query parameters
            :path_params: list of path parameters
            :query_params: dict of query parameters
            :return: None
            """
            for key, value in query_params.items():
                if value is None:
                    continue
                if key in self.query_parameters.values():
                    self.parameters['query'][key] = str(value).encode('utf-8')
                elif key in self.query_parameters.keys():
                    self.parameters['query'][self.query_parameters[key]] = str(value).encode('utf-8')

            for value in path_params:
                self.parameters['path'].append(value.encode('utf-8'))

            self.parameters['query']['_format'] = self.client.format
            self.parameters['query']['key'] = self.client.api_key
            self.parameters['query']['locale'] = self.client.locale
            self.parameters['query']['cur'] = self.client.currency

        def _prepare_request(self):
            """
            Prepares url and query parameters for the request
            :return: Tuple with two elements, url and query parameters
            """
            url_parts = {
                'protocol': self.client.protocol,
                'base_url': self.client.base_url,
                'base_path': self.client.base_path,
                'api_path': self.api_path,
            }
            url = '{protocol}://{base_url}{base_path}{api_path}'.format(**url_parts)

            url_parts = self.parameters['path']
            url_parts.insert(0, url)

            url = '/'.join([part if type(part) == str else part.decode('utf-8') for part in url_parts])

            self.debug.ok('url', url)
            self.debug.ok('query_parameters', self.parameters['query'])

            return url, self.parameters['query']

        def _do_request(self, url, params):
            """
            Makes the request to BlaBlaCar Api servers
            :url: Url for the request
            :params: Query parameters
            :return: Tuple with two elements, status code and content
            """
            if self.method == 'GET':
                response = requests.get(url, params=params)
                self.debug.ok('response_object', response)
                return response.status_code, response.json()
            else:
                # For future POST, PUT, DELETE requests
                pass

        def _proccess_response(self, status_code, response):
            """
            Process response using models
            :status_code: Response status code
            :response: Content
            :return: Model with the data from the response
            """
            if status_code != 200:
                self.debug.error('status_code', status_code)
                self.debug.error('response', response)

                if 'message' in response:
                    raise BlaBlaCarRequestApiException(response['message'])
                if 'error' in response:
                    raise BlaBlaCarRequestApiException(response['error'].get('message', 'Unknown error occurred!'))
                else:
                    raise BlaBlaCarRequestApiException('Unknown error occurred!')
            else:
                self.debug.ok('status_code', status_code)
                self.debug.ok('response', response)

            return self.model.proccess(response)

        def _call(self):
            """
            Makes the API call
            :return: Return value from self._proccess_response()
            """
            url, params = self._prepare_request()
            status_code, response = self._do_request(url, params)
            return self._proccess_response(status_code, response)

    def call(client, *path_params, **query_params):
        """
        Binded method for API calls
        :path_params: list of path parameters
        :query_params: dict of query parameters
        :return: Return value from ApiRequest._call()
        """
        with Debug(client=client) as debug:
            request = ApiRequest(client, debug, *path_params, **query_params)
            return request._call()

    return call
