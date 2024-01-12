# GeoDist: Manual implementation of the Haversine (great-circle) distance between two geospatial coordinates

To do:
- [x] Update README with installation, usage, etc. 
- [ ] Write unit tests
- [ ] Change import usage to accept list(s) of coordinate points
- [ ] Add CLI arg for specifying lat long vs long lat

Installation:
Clone this repository, cd into the directory, `pip install .`

Package import usage:
```python

from geodist import haversine_distance
dist = haversine_distance(38.89220430021896, -77.05003345757281, 38.892175669253966, -77.02004891843859, 'km')
print(dist)
```

CLI usage:
```
usage: geodist [-h] --coordinates [COORDINATES ...] [--unit UNIT]

optional arguments:
  -h, --help            show this help message and exit
  --coordinates [COORDINATES ...]
                        Latitude1 Longitude1 Latitude2 Longitude2
  --unit UNIT           Earth unit for Haversine distance metric.
```

Example: `geodist --coordinates 38.89220430021896 -77.05003345757281 38.892175669253966 -77.02004891843859`