from datetime import datetime


__author__ = 'ivan.arar@gmail.com'


class Model(object):

	@classmethod
	def proccess(cls, params):
		return cls(**params)

	def convert_datetime(self, date_time):
		try:
			dt = date_time.split(' ')
			d = dt[0].split('/')
			t = dt[1].split(':')
			return datetime(int(d[2]), int(d[1]), int(d[0]), int(t[0]), int(t[1]), int(t[2]))
		except:
			return date_time


class Trip(Model):

	def __init__(self, **params):
		self.departure_date = self.convert_datetime(params.get('departure_date'))

		self.links = params.get('links')
		self.frequency = params.get('frequency')
		self.arrival_place = params.get('arrival_place')
		self.price = params.get('price')
		self.departure_place = params.get('departure_place')
		self.price_with_commission = params.get('price_with_commission')
		self.seats_left = params.get('seats_left')
		self.seats = params.get('seats')
		self.duration = params.get('duration')
		self.distance = params.get('distance')
		self.permanent_id = params.get('permanent_id')
		self.car = params.get('car')
		self.viaggio_rosa = params.get('viaggio_rosa')
		self.is_comfort = params.get('is_comfort')
		self.freeway = params.get('freeway')
		self.booking_mode = params.get('booking_mode')
		self.booking_type = params.get('booking_type')
		self.locations_to_display = params.get('locations_to_display')
