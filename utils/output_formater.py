from enum import Enum
from typing import NamedTuple

from . import config
from .weather_service import Weather


class UnitDescription(NamedTuple):
    name: str
    temperature: str
    speed: str


class MeasurementUnits(Enum):
    STANDARD = UnitDescription('standard', 'K.', 'm/s')
    METRIC = UnitDescription('metric', '°', 'm/s')
    IMPERIAL = UnitDescription('imperial', 'F.', 'mil/h')


def get_weather_output(weather: Weather) -> str:
    """Форматирует поля ``weather`` в строку для вывода в консоль"""

    formatted_string = _create_weather_output(weather)
    return formatted_string


def _create_weather_output(weather: Weather) -> str:
    formatted_string = config.OUTPUT_TEXT.format(
        country=weather.country,
        city=weather.city,
        min_temperature=_format_temperature_output(weather.min_temperature),
        max_temperature=_format_temperature_output(weather.max_temperature),
        dawn=weather.dawn.strftime(config.TIME_STR_FORMAT),
        sunset=weather.sunset.strftime(config.TIME_STR_FORMAT)
    )

    return formatted_string


def _format_temperature_output(temperature: int | str) -> str:
    if not config.OPENWEATHER_API_PARAMETERS['units']:
        temperature = str(temperature) + MeasurementUnits.STANDARD.value.temperature
    else:
        temperature_format = [
            unit for unit in MeasurementUnits if unit.value.name == config.OPENWEATHER_API_PARAMETERS['units']
        ][0]
        temperature = str(temperature) + temperature_format.value.temperature

    return temperature
