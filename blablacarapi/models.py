from datetime import datetime

from blablacarapi.paging import Paging


__author__ = 'ivan.arar@gmail.com'


class Model(object):

    @classmethod
    def proccess(cls, params):
        if type(params) == dict:
            return cls(**params)
        if type(params) == list:
            return [cls(**child_params) for child_params in params]

    def convert_datetime(self, date_time):
        try:
            dt = date_time.split(' ')
            d = dt[0].split('/')
            t = dt[1].split(':')
            return datetime(int(d[2]), int(d[1]), int(d[0]), int(t[0]), int(t[1]), int(t[2]))
        except:
            return date_time


class Trips(Model):

    def __init__(self, **params):
        self.pager = Paging(params.get('pager'))
        self.trips = Trip.proccess(params.get('trips'))
        self.top_trips = Trip.proccess(params.get('top_trips'))

        self.facets = params.get('facets')
        self.savings = params.get('savings')
        self.distance = params.get('distance')
        self.duration = params.get('duration')
        self.recommended_price = params.get('recommended_price')


class Trip(Model):

    def __init__(self, **params):
        self.departure_date = self.convert_datetime(params.get('departure_date'))

        self.car = params.get('car')
        self.links = params.get('links')
        self.price = params.get('price')
        self.seats = params.get('seats')
        self.freeway = params.get('freeway')
        self.duration = params.get('duration')
        self.distance = params.get('distance')
        self.frequency = params.get('frequency')
        self.seats_left = params.get('seats_left')
        self.is_comfort = params.get('is_comfort')
        self.permanent_id = params.get('permanent_id')
        self.viaggio_rosa = params.get('viaggio_rosa')
        self.booking_mode = params.get('booking_mode')
        self.booking_type = params.get('booking_type')
        self.arrival_place = params.get('arrival_place')
        self.departure_place = params.get('departure_place')
        self.locations_to_display = params.get('locations_to_display')
        self.price_with_commission = params.get('price_with_commission')
