from configparser import ConfigParser
from enum import Enum


class ConfigFileError(Exception):
    pass


class ErrorStatuses(Enum):
    WRONG_PATH = 'Неверный путь к конфиг файлу.'
    WEATHER_SECTION = 'Конфигурационный файл не содержит секции Weather.'
    DEFAULT_CITY = 'Конфигурационный файл не содержит значение default_city.'


class ConfigFile:

    def __init__(self, config_file_name: str = 'config.cfg'):
        self._read_and_setup_config(config_file_name)
        self.default_city: str

    def _read_and_setup_config(self, config_file_name: str) -> None:
        config_file = self._read_config_file(config_file_name)
        self._setup_config(config_file)

    def _read_config_file(self, config_file_name: str) -> ConfigParser:
        config_file = ConfigParser()
        config_file.read(config_file_name)

        if self._check_config_file(config_file):
            return config_file

    @staticmethod
    def _check_config_file(config_file: ConfigParser) -> bool:
        if not config_file.sections():
            raise ConfigFileError(ErrorStatuses.WRONG_PATH.value)
        if 'Weather' not in config_file.sections():
            raise ConfigFileError(ErrorStatuses.WEATHER_SECTION.value)
        if not config_file.get('Weather', 'default_city'):
            raise ConfigFileError(ErrorStatuses.DEFAULT_CITY.value)

        return True

    def _setup_config(self, config_file: ConfigParser) -> None:
        self.default_city = config_file['Weather']['default_city']


config = ConfigFile()
