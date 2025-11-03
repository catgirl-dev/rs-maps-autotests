import json
from typing import Any
from requests import Response
from logger_config import logger


class Checking:
    """Проверки для тестов"""
    @staticmethod
    def check_status_code(response: Response, expected_status_code: int):
        """Проверка статус-кода"""
        assert response.status_code == expected_status_code, \
            (f"Ошибка при проверке статус-кода. Статус-код: {response.status_code}. "
             f"Ожидаемый статус-код: {expected_status_code}")
        logger.success(f"Проверка статус-кода пройдена. Статус код: {response.status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value: Any):
        """Проверка наличия обязательных полей"""
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Отсутствуют обязательные поля"
        logger.success("Все ожидаемые поля присутствуют")

    @staticmethod
    def check_json_filds(response: Response, field_name: str, expected_value: Any):
        """Проверка содержимого обязательных полей"""
        check = response.json
        check_info: Any = check.get(field_name)
        assert check_info == expected_value, (f"Содержимое поля {field_name} "
                                              f"не соответствует ожидаемому {expected_value}")
        logger.success(f"Проверка содержимого поля {field_name} прошла успешно!")