import os

from dotenv import load_dotenv


load_dotenv()

DEFAULT_CITY = 'Dnepropetrovsk'
INTEGER_DEGREE = True

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
OPENWEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'
OPENWEATHER_API_PARAMETERS = {
    'exclude': None,
    'units': 'metric',
    'lang': 'ru',
}

OUTPUT_TEXT = """
{country}, {city}

Минимальная температура: {min_temperature}
Максимальная температура: {max_temperature}
Рассвет: {dawn}
Закат: {sunset}
"""

TIME_STR_FORMAT = '%H:%M:%S'
