import unittest
from geodist.haversine import haversine_distance


class TestHaversine(unittest.TestCase):
    def test_haversine_km(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "km",
        )
        self.assertAlmostEqual(result, 2.595, 2)

    def test_haversine_mi(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "mi",
        )
        self.assertAlmostEqual(result, 1.613, 2)

    def test_haversine_m(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "m",
        )
        self.assertAlmostEqual(result, 2595.783, 2)

    def test_haversine_ft(self):
        result = haversine_distance(
            38.89220430021896,
            -77.05003345757281,
            38.892175669253966,
            -77.02004891843859,
            "ft",
        )
        self.assertAlmostEqual(result, 8516.349, 2)


if __name__ == "__main__":
    unittest.main()
