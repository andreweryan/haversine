import pytest
from haversine import haversine_distance


def test_haversine_mi():
    result = haversine_distance(
        38.89220430021896,
        -77.05003345757281,
        38.892175669253966,
        -77.02004891843859,
        "miles",
    )
    assert abs(result - 1.613) < 0.1


def test_haversine_m():
    result = haversine_distance(
        38.89220430021896,
        -77.05003345757281,
        38.892175669253966,
        -77.02004891843859,
        "meters",
    )
    assert abs(result - 2595.0534) < 0.1


def test_haversine_ft():
    result = haversine_distance(
        38.89220430021896,
        -77.05003345757281,
        38.892175669253966,
        -77.02004891843859,
        "feet",
    )
    assert abs(result - 8513.955) < 0.1
