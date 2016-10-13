from models import Trip
from bind import bind_request
from exceptions import BlaBlaCarRequestApiException


__author__ = 'ivan.arar@gmail.com'


class Client(object):

	base_url = 'public-api.blablacar.com'
	base_path = '/api/v2'
	protocol = 'https'
	format = 'json'

	def __init__(self, api_key=None):
		if not api_key:
			raise BlaBlaCarRequestApiException('API key missing!')
		self.api_key = api_key

	trips = bind_request(
		api_path = '/trips',
		response_root = 'trips',
		model = Trip,
		parameters_map = {
			# required parameters
			'locale': 'locale', 'currency': 'cur', 

			# locations
			'frm': 'fn', 'to': 'tn', 'from_coordinate': 'fc', 'to_coordinate': 'tc', 

			# dates and hours
			'date_from': 'db', 'date_to': 'de', 'hour_from': 'hb', 'hour_to': 'he', 

			# other seaerch params
			'seats': 'seats', 'photo': 'photo', 'radius': 'radius', 

			# return data
			'page': 'page', 'return_fields': 'fields', 

			# sort, order, limit
			'sort': 'sort', 'order': 'order', 'limit': 'limit',
		}
	)