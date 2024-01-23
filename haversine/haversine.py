from math import sqrt, sin, cos, asin, radians


def haversine_distance(
    lat1: float, lon1: float, lat2: float, lon2: float, unit: str = "kilometers"
) -> float:
    """Calculate the Haversine (great-circle) distance between two geospatial coordinates.

    Args:
        lat1 (float): Point 1 Latitude
        lon1 (float): Point 1 Longitude
        lat2 (float): Point 2 Latitude
        lon2 (float): Point 2 Longitude
        unit (str): Earth unit for Haversine distance metric.
    Returns:
        distance (float): Haversine Distance between two points
    """

    earth_radius = {
        "kilometers": 6371.009,
        "meters": 6371009,
        "miles": 3958.7614581,
        "feet": 20902260.49876800925,
    }

    r = earth_radius.get(unit)

    if not r:
        raise ValueError("Units not specified.")

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1

    dlon = lon2 - lon1

    h = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    h = min(1, h)

    arc = 2 * asin(sqrt(h))

    distance = arc * r

    return distance
