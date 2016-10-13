<h1>BlaBlaCar Client Api Python Library</h1>

<p>Easily search for trips!</p>

<h3>Installation</h3>

```
pip install git+git://github.com/arrrlo/BlaBlaCar-Client-Api@master
```

<h3>Usage</h3>

```
from blablacar import BlaBlaCarApi

# initialize API
api = BlaBlaCarApi(api_key="__your_blablacar_api_key_here__")

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
	print("%s: %s -> %s" % (trip.departure_date, 
							trip.departure_place['address'], 
							trip.arrival_place['address']))

	# fetch data for one trip using trip id
	single_trip = api.trip(trip.permanent_id)

# paging
trips.pager.has_next() # True or False
trips.pager.next() # returns 2 if the current page is 1
trips.pager.previous() # returns False if the current page is 1, and it returns 1 if current page is 1
```

<p>Works on both 2.7.x and 3.x python.</p>

<h3>Official documentation</h3>

<p>For more information visit oficial documentation: <a href="https://dev.blablacar.com/docs/versions/1.0">https://dev.blablacar.com/docs/versions/1.0</a></p>