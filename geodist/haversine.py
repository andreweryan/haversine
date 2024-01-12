from math import sqrt, sin, cos, asin, radians


def haversine_distance(
    lat1: float, lon1: float, lat2: float, lon2: float, unit: str
) -> float:
    """
    Calculate the Haversine (great-circle) distance between two geospatial coordinates

    Args:
        lat1 (float): Point 1 Latitude
        lon1 (float): Point 1 Longitude
        lat2 (float): Point 2 Latitude
        lon2 (float): Point 2 Longitude
        unit (str): Earth unit for Haversine distance metric.
    Returns:
        distance (float): Haversine Distance between two points
    """

    if unit == "mi":
        units = 3959.87433
    elif unit == "ft":
        units = 20908136.4624
    elif unit == "km":
        units = 6372.8
    elif unit == "m":
        units = 6372800
    else:
        raise ValueError("Units not specified.")

    r = units

    dLat = radians(lat2 - lat1)

    dLon = radians(lon2 - lon1)

    lat1 = radians(lat1)

    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2

    c = 2 * asin(sqrt(a))

    distance = r * c

    return distance
