import os
import requests

from api_exceptions import BlaBlaCarRequestApiException


__author__ = 'ivan.arar@gmail.com'


def bind_request(**request_data):

    class ApiRequest(object):

        model = request_data.get('model')
        api_path = request_data.get('api_path')
        method = request_data.get('method', 'GET')
        query_parameters = request_data.get('query_parameters')

        def __init__(self, client, *path_params, **query_params):
            self.client = client
            self.parameters = {'query': {}, 'path': []}
            self._set_parameters(*path_params, **query_params)

        def _set_parameters(self, *path_params, **query_params):
            self.query_parameters = dict(list(self.query_parameters.items()) + 
                                         list(self.client.standard_query_parameters.items()))
            
            for key, value in query_params.items():
                if value is None:
                    continue
                if key in self.query_parameters.values():
                    self.parameters['query'][key] = str(value).encode('utf-8')
                elif key in self.query_parameters.keys():
                    self.parameters['query'][self.query_parameters[key]] = str(value).encode('utf-8')

            for value in path_params:
                self.parameters['path'].append(value.encode('utf-8'))
            
            self.parameters['query']['format'] = self.client.format
            self.parameters['query']['key'] = self.client.api_key

            if 'locale' not in self.parameters['query']:
                if os.environ.get('LC_ALL'):
                    self.parameters['query']['locale'] = os.environ['LC_ALL']

        def _prepare_request(self):
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

            return url, self.parameters['query']

        def _do_request(self, url, params):
            if self.method == 'GET':
                req = requests.get(url, params=params)
                return req.status_code, req.json()
            else:
                # For future POST, PUT, DELETE requests
                pass

        def _proccess_response(self, status_code, response):
            if status_code != 200:
                if 'message' in response:
                    raise BlaBlaCarRequestApiException(response['message'])
                if 'error' in response:
                    raise BlaBlaCarRequestApiException(response['error'].get('message', 'Unknown error occurred!'))
                else:
                    raise BlaBlaCarRequestApiException('Unknown error occurred!')
            
            return self.model.proccess(response)

        def _call(self):
            url, params = self._prepare_request()
            status_code, response = self._do_request(url, params)
            return self._proccess_response(status_code, response)

    def call(client, *path_params, **query_params):
        request = ApiRequest(client, *path_params, **query_params)
        return request._call()

    return call
