__author__ = 'ivan.arar@gmail.com'


class Model(object):

	@classmethod
	def proccess(cls, params):
		return cls(**params)


class Trip(Model):

	def __init__(self, **params):
		self.links = params.get('links')
		self.frequency = params.get('frequency')
		self.departure_date = params.get('departure_date')
		self.departure_place = params.get('departure_place')
		self.arrival_place = params.get('arrival_place')
		self.price = params.get('price')
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
