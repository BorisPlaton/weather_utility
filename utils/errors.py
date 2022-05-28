class CantGetResponseError(Exception):
    """Ошибка сетевого запроса"""
    pass


class WrongCityError(Exception):
    """Неверное указание названия города"""
    pass
