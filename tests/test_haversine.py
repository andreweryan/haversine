import unittest
from haversine import haversine_distance


class TestHaversine(unittest.TestCase):
    def test_haversine_km(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "kilometers",
        )
        self.assertAlmostEqual(result, 2.595, 1)

    def test_haversine_mi(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "miles",
        )
        self.assertAlmostEqual(result, 1.613, 1)

    def test_haversine_m(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "meters",
        )
        self.assertAlmostEqual(result, 2595.0534, 1)

    def test_haversine_ft(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "feet",
        )
        self.assertAlmostEqual(result, 8513.955, 1)


if __name__ == "__main__":
    unittest.main()
