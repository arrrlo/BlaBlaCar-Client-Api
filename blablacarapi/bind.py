import requests

from exceptions import BlaBlaCarRequestApiException


__author__ = 'ivan.arar@gmail.com'


def bind_request(**request_data):

    class ApiRequest(object):

        model = request_data.get('model')
        api_path = request_data.get('api_path')
        method = request_data.get('method', 'GET')
        response_root = request_data.get('response_root')
        parameters_map = request_data.get('parameters_map')

        def __init__(self, client, **kwargs):
            self.client = client
            self.parameters = {}
            self._set_parameters(**kwargs)

        def _set_parameters(self, **kwargs):
            for key, value in kwargs.items():
                if value is None:
                    continue
                if key in self.parameters_map.values():
                    self.parameters[key] = value.encode('utf-8')
                elif key in self.parameters_map.keys():
                    self.parameters[self.parameters_map[key]] = value.encode('utf-8')
            
            self.parameters['format'] = self.client.format
            self.parameters['key'] = self.client.api_key

        def _prepare_request(self):
            url_parts = {
                'protocol': self.client.protocol,
                'base_url': self.client.base_url,
                'base_path': self.client.base_path,
                'api_path': self.api_path,
            }
            url = '{protocol}://{base_url}{base_path}{api_path}'.format(**url_parts)
            return url, self.parameters

        def _do_request(self, url, params):
            if self.method == 'GET':
                req = requests.get(url, params=params)
                return req.status_code, req.json()
            else:
                # For future POST, PUT, DELETE requests
                pass

        def _proccess_content(self, status_code, content):
            if status_code != 200:
                if 'message' in content:
                    raise BlaBlaCarRequestApiException(content['message'])
                else:
                    raise BlaBlaCarRequestApiException('Unknown error occurred!')
            list_models = []
            for item in content[self.response_root]:
                list_models.append(self.model.proccess(item))
            return list_models

        def _call(self):
            url, params = self._prepare_request()
            status_code, content = self._do_request(url, params)
            return self._proccess_content(status_code, content)

    def call(client, **kwargs):
        request = ApiRequest(client, **kwargs)
        return request._call()

    return call