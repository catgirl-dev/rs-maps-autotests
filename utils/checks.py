import json

from requests import Response


class Checking:
    """Проверки для тестов"""
    # Проверка статус-кода
    @staticmethod
    def check_status_code(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            (f"Ошибка при проверке статус-кода. Статус-код: {response.status_code}. "
             f"Ожидаемый статус-код: {expected_status_code}")
        print(f"Проверка статус-кода пройдена. Статус код: {response.status_code}")

    # Проверка наличия обязательных полей
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, f"Отсутствуют обязательные поля"
        print("Все ожидаемые поля присутствуют")