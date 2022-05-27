import argparse
from typing import NamedTuple

from utils.config import config


class ParserValues(NamedTuple):
    city: str


def get_parser_values() -> ParserValues:
    parser = argparse.ArgumentParser(description="Показывает погоду в городе.")
    parser.add_argument(
        '-c', '--city', type=str, help="Город, о котором будет выведена информация.", default=config.default_city
    )
    args = parser.parse_args()

    return ParserValues(args.city)
