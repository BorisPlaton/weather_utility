from datetime import datetime
from enum import Enum
from typing import NamedTuple

from .coordinates import Coordinates


class WeatherType(Enum):
    Thunderstorm = 'Гроза'
    Drizzle = 'Изморозь'
    Rain = 'Дождь'
    Snow = 'Снег'
    Clear = 'Ясно'
    Fog = 'Туман'
    Clouds = 'Облачно'


class Weather(NamedTuple):
    temperature: float
    weather_type: WeatherType
    dawn: datetime
    sunset: datetime
    city: str


def get_weather_info(coordinates: Coordinates) -> Weather:
    """Получает информацию о погоде по координатам"""
    pass
