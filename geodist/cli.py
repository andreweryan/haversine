import argparse
from .haversine import haversine_distance


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--coordinates",
        nargs="*",
        required=True,
        help="Latitude1 Longitude1 Latitude2 Longitude2",
    )
    parser.add_argument(
        "--unit",
        type=str,
        default="km",
        choices=["km", "mi", "m", "ft"],
        help="Earth unit for Haversine distance metric.Default=km",
    )

    args = parser.parse_args()

    coords = list(map(float, args.coordinates))

    distance = haversine_distance(coords[0], coords[1], coords[2], coords[3], args.unit)

    print(distance)


if __name__ == "__main__":
    """
    38.89220430021896 -77.05003345757281 38.892175669253966 -77.02004891843859
    mi: 1.613, km: 2.595, ft: 8516.349, m: 2595.783

    """

    main()
