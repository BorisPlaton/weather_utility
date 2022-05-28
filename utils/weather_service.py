from datetime import datetime
from enum import Enum
from typing import NamedTuple

import requests
from dateutil.tz import tz

from . import config
from .coordinates import Coordinates
from .errors import CantGetResponseError


class WeatherType(Enum):
    Thunderstorm = 'Гроза'
    Drizzle = 'Изморозь'
    Rain = 'Дождь'
    Snow = 'Снег'
    Clear = 'Ясно'
    Fog = 'Туман'
    Clouds = 'Облачно'


class Weather(NamedTuple):
    min_temperature: float | int
    max_temperature: float | int
    weather_type: WeatherType
    dawn: datetime
    sunset: datetime
    country: str
    city: str


def get_weather_info(coordinates: Coordinates) -> Weather:
    """Получает информацию о погоде по координатам"""
    weather_data = _get_weather_data_by_coordinates(coordinates)
    return weather_data


def _get_weather_data_by_coordinates(coordinates: Coordinates) -> Weather:
    response = _send_openweather_request(coordinates)
    weather_data = _collect_weather_data_from_response(response)
    return weather_data


def _send_openweather_request(coordinates: Coordinates) -> requests.Response:
    request_params = {
        'lat': coordinates.latitude,
        'lon': coordinates.longitude,
        'appid': config.OPENWEATHER_API_KEY,
    }
    request_params.update(config.OPENWEATHER_API_PARAMETERS)

    response = requests.get(
        config.OPENWEATHER_API_URL,
        params=request_params,
    )
    if not 200 <= response.status_code < 300:
        status_code = response.status_code
        message = response.json().get('message')
        raise CantGetResponseError(f"{status_code}. {message}")

    return response


def _collect_weather_data_from_response(response: requests.Response) -> Weather:
    response = response.json()
    weather_info = Weather(
        min_temperature=_format_temperature_type(response['main']['temp_min']),
        max_temperature=_format_temperature_type(response['main']['temp_max']),
        weather_type=response['weather'][0]['main'],
        dawn=_format_datetime(response['sys']['sunrise'], response['timezone']),
        sunset=_format_datetime(response['sys']['sunset'], response['timezone']),
        country=response['sys']['country'],
        city=response['name']
    )

    return weather_info


def _format_temperature_type(temperature_degree: int | float) -> int | float:
    temperature = int(temperature_degree) if config.INTEGER_DEGREE else round(temperature_degree, 1)

    return temperature


def _format_datetime(time: int, timezone: int) -> datetime:
    tz_class = tz.tzoffset('IST', timezone)
    datetime_with_tz = datetime.fromtimestamp(time, tz=tz_class)
    return datetime_with_tz
