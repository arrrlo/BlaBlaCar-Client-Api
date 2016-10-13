<h1>BlaBlaCar Client Api</h1>

<p>Easily search for trips!</p>

<h3>Instalation</h3>

```
pip install git+git://github.com/arrrlo/BlaBlaCar-Client-Api@master
```

<h3>Usage</h3>

```
from blablacar import BlaBlaCarApi

api = BlaBlaCarApi(api_key="__your_blablacar_api_key_here__")
trips = api.trips(frm="London", to="Paris")

for trip in trips:
	print("%s: %s -> %s" % (trip.departure_date, 
							trip.departure_place['address'], 
							trip.arrival_place['address']))
```

