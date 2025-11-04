import allure
import requests

from requests import Response


class HttpMethods:
    """Список HTTP методов"""
    headers: dict[str, str] = {'Content-Type': 'application/json'}
    cookie: dict[str, str] = {}

    @staticmethod
    def post(url, body):
        with allure.step("POST request"):
            result: Response = requests.post(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body)
            return result

    @staticmethod
    def get(url):
        with allure.step("GET request"):
            result: Response = requests.get(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT request"):
            result: Response = requests.put(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE request"):
            result: Response = requests.delete(
                url,
                headers=HttpMethods.headers,
                cookies=HttpMethods.cookie,
                json=body)
            return result
