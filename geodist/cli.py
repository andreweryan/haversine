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
        choices=["kilometers", "miles", "meters", "feet"],
        help="Earth unit for Haversine distance metric. Default=km",
    )

    args = parser.parse_args()

    coords = list(map(float, args.coordinates))

    distance = haversine_distance(coords[0], coords[1], coords[2], coords[3], args.unit)

    print(distance)


if __name__ == "__main__":
    main()
