<h1>BlaBlaCar API Client Python Library</h1>

[![PyPI version](https://badge.fury.io/py/BlaBlaCar-API.svg)](https://badge.fury.io/py/BlaBlaCar-API)

<p>Easily search for trips!</p>

<h3>Installation</h3>
<p>Works on both 2.7.x and 3.x python.</p>

```
pip install blablacar-api
```

<h3>Usage</h3>

```python
from blablacarapi import BlaBlaCarApi

# initialize API
api = BlaBlaCarApi(api_key="__your_api_key_here__")

# fetch trips from London to Paris
trips = api.trips(frm="London", to="Paris")

# after fetching you have:
# trips.trips
# trips.top_trips
# trips.pager
# trips.facets
# trips.savings
# trips.distance
# trips.duration
# trips.recommended_price

# iterate over the trips
for trip in trips.trips:
	print("%s: %s -> %s" % (trip.departure_date, trip.departure_place['address'], trip.arrival_place['address']))
	# fetch data for one trip using trip id
	single_trip = api.trip(trip.permanent_id)

# paging
trips.pager.has_next() # True or False
trips.pager.next() # returns 2 if the current page is 1
trips.pager.has_previous() # True or False
trips.pager.previous() # returns False if the current page is 1, and it returns 1 if current page is 2
```

<h3>Locales</h3>

```python
api = BlaBlaCarApi(api_key="__your_blablacar_api_key_here__", locale="en_GB", currency="en_GB")
```

<h3>Debugging</h3>

<p>If you want to debug your code using the data regarding the API call.</p>

```python
# initialize with debug=True
api = BlaBlaCarApi(api_key="...", debug=True)

# after every API call the client library will automatically print all the data to standard output
api.trips(...)

# and you can always have all debug data in your code
debug_data = api.request.debug.show()
```

<h3>Official documentation</h3>

<p>For more information visit official documentation: <a href="https://dev.blablacar.com/docs/versions/1.0">https://dev.blablacar.com/docs/versions/1.0</a></p>
