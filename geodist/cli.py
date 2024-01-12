import argparse
from .haversine import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('--coordinates', nargs='*', required=True, help=" ")
    parser.add_argument('--unit', type=str, default='km', help="Earth unit for Haversine distance metric.")

    args = parser.parse_args()

    coords = list(map(float, args.coordinates))

    distance = haversine(coords[0], coords[1], coords[2], coords[3], args.unit)
    print(distance)

if __name__ == "__main__":
    
    """
    TODO:
    - write unit tests
    - add flag for lon/lat vs lat/lon


    38.89220430021896 -77.05003345757281 38.892175669253966 -77.02004891843859
    mi: 1.613, km: 2.595, ft: 8516.349, m: 2595.783

    """
    
    main()