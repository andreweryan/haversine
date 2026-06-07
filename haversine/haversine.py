import numpy as np

EARTH_RADIUS_KM = 6371.009

def haversine_distance(
    lat1,
    lon1,
    lat2,
    lon2,
    radius=EARTH_RADIUS_KM,
):
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2.0) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2.0) ** 2
    )

    a = np.clip(a, 0.0, 1.0)

    return 2 * radius * np.arcsin(np.sqrt(a))
