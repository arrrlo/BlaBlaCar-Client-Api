import pprint


__author__ = 'ivan.arar@gmail.com'


STATUS_OK = 'ok'
STATUS_ERROR = 'error'


class Debug(object):

    def __init__(self, client):
        self.client = client
        self.recorded_data = {}
        self.output = StandardOutput()

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if self.client.debug:
            self.standard_output()

    def ok(self, key, value):
        self.record(key, value, STATUS_OK)

    def error(self, key, value):
        self.record(key, value, STATUS_ERROR)

    def record(self, key, value, status):
        if self.client.debug:
            self.recorded_data[key] = {'value': value, 'status': status}

    def show(self, standard_output=False):
        if standard_output:
            self.standard_output()
        else:
            return self.recorded_data

    def standard_output(self):
        self.output.plain('')
        self.output.green('BlaBlaCar API Client Debug')
        self.output.green('----------------------------------------------------------')

        for key, value in self.recorded_data.items():
            if value['status'] == STATUS_OK:
                output_method = self.output.blue
            if value['status'] == STATUS_ERROR:
                output_method = self.output.error

            value = value['value']
            if type(value) == object:
                value = dir(value)

            output_method('%s: [%s] %s' % (str(key), 
                                           str(type(value)), 
                                           pprint.pformat(value)))

        self.output.green('----------------------------------------------------------')
        self.output.plain('')


class StandardOutput(object):

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def base_message(self, m_type, message, end=None):
        if end is None:
            end = self.ENDC
        print('%s%s%s' % (m_type, message, end))
    
    def plain(self, message):
        self.base_message('',message,'')

    def blue(self, message):
        self.base_message(self.BLUE, message)

    def green(self, message):
        self.base_message(self.GREEN, message)

    def warning(self, message):
        self.base_message(self.WARNING, message)

    def error(self, message):
        self.base_message(self.ERROR, message)

    def bold(self, message):
        self.base_message(self.BOLD, message)

