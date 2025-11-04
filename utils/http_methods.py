import allure
import requests

from requests import Response


import requests
import allure
from requests import Response

class HttpMethods:
    """Список HTTP методов"""
    headers: dict[str, str] = {'Content-Type': 'application/json'}
    cookie: dict[str, str] = {}

    @staticmethod
    def post(url, body) -> Response:
        with allure.step(f"POST request to {url}"):
            result: Response = requests.post(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body
            )
            allure.attach(result.text, name="Response body", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def get(url) -> Response:
        with allure.step(f"GET request to {url}"):
            result: Response = requests.get(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie
            )
            allure.attach(result.text, name="Response body", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def put(url, body) -> Response:
        with allure.step(f"PUT request to {url}"):
            result: Response = requests.put(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body
            )
            allure.attach(result.text, name="Response body", attachment_type=allure.attachment_type.JSON)
            return result

    @staticmethod
    def delete(url, body) -> Response:
        with allure.step(f"DELETE request to {url}"):
            result: Response = requests.delete(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body
            )
            allure.attach(result.text, name="Response body", attachment_type=allure.attachment_type.JSON)
            return result

