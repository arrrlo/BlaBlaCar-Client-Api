from blablacarapi.models import Trip, Trips
from blablacarapi.bind import bind_request
from blablacarapi.api_exceptions import BlaBlaCarRequestApiException


__author__ = 'ivan.arar@gmail.com'


class Client(object):

    base_url = 'public-api.blablacar.com'
    base_path = '/api/v2'
    protocol = 'https'
    format = 'json'

    def __init__(self, api_key=None, locale=None, currency=None, debug=False):
        if not api_key:
            raise BlaBlaCarRequestApiException('API key missing!')
        self.api_key = api_key
        self.locale = locale
        self.currency = currency
        self.debug = debug

    trips = bind_request(
        api_path='/trips',
        model=Trips,
        query_parameters={
            'frm': 'fn',  # From Name: the departure place name
            'to': 'tn',  # To Name: the arrival place name

            'page': 'page',  # Number of the requested page of result, if there is more than 1 page
            'sort': 'sort',  # Sorting parameter of the query. Possible values are: "trip_date" or "trip_price"
            'order': 'order',  # Order of the sorting. Only used in combination with "sort".
            # Possible values are: "asc" or "desc"
            'limit': 'limit',  # Maximum number of results requested.
            # May results in slower and bigger queries. Must be < 100
            'return_fields': 'fields',  # Limit the response to the mentioned fields of the return values

            'hour_from': 'hb',  # Hour Begin: hour of the earliest departure time. must be >= 0 and < 24
            'hour_to': 'he',  # Hour End: hour of the earliest departure time. must be > 0 and <= 24 and > hb
            'date_from': 'db',  # Date Begin: exact date of the requested search if no "de" parameter is present or
                               # begin of the period of the requested search,
                               # if there is also a "de" parameter Format: "DDDD-MM-YY" or "DDDD-MM-YY HH:mm:ss"
            'date_to': 'de',  # Date End: end of the range of the requested search
                             # Format: "DDDD-MM-YY" or "DDDD-MM-YY HH:mm:ss"

            'seats': 'seats',  # number of requested available seats
            'photo': 'photo',  # Limit results to trips with or without driver pictures

            'radius': 'radius',  # Maximum radius of the search, in km Default is 10% of the length of the trip
            'to_coordinate': 'tc',  # To Coordinate, as: "float|float",
            # will be prefered to the "tn" parameter if both are presents
            'from_coordinate': 'fc',  # From Coordinate, as: "float|float",
            # will be prefered to the "fn" parameter if both are presents
        }
    )

    trip = bind_request(
        api_path='/trips',
        model=Trip,
        query_parameters={}
    )
