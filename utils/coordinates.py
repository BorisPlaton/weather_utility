from typing import NamedTuple

from geopy import Nominatim

from utils.errors import WrongCityError


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_city_coordinates(city: str) -> Coordinates:
    """Возвращает GPS координаты по названию города"""

    return _get_latitude_and_longitude_of_the_city(city)


def _get_latitude_and_longitude_of_the_city(city: str) -> Coordinates:
    loc = Nominatim(user_agent="GetLoc")
    location_info = loc.geocode(city)

    if not location_info:
        raise WrongCityError('Неверное название города.')

    return Coordinates(location_info.latitude, location_info.longitude)
