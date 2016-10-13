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

# iterate over the results
for trip in trips:
	print("%s: %s -> %s" % (trip.departure_date, 
							trip.departure_place['address'], 
							trip.arrival_place['address']))

	# fetch data for one trip using trip id
	single_trip = api.trip(trip.permanent_id)
```

<p>Works on both 2.7.x and 3.x python.</p>