from setuptools import setup, find_packages


setup(
    name="haversine",
    version="0.0.1",
    author="Andrew Ryan",
    author_email="aryanvt15@proton.me",
    description="Tool for calculating haversine distance between two geospatial coordinates.",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["haversine = haversine.cli:main"],
    },
)
