from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_city_coordinates(city: str) -> Coordinates:
    """Возвращает GPS координаты по названию города"""
    pass
