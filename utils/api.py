import allure
from requests import Response

from utils.http_methods import HttpMethods
from logger_config import logger

BASE_URL: str = "https://rahulshettyacademy.com"
KEY: str = "key=qaclick123"
GET_RESOURCE: str = "/maps/api/place/get/json"
POST_RESOURCE: str = "/maps/api/place/add/json"
PUT_RESOURCE: str = "/maps/api/place/update/json"
DELETE_RESOURCE: str = "/maps/api/place/delete/json"



class RsMapsApi:
    """Методы для тестирования RS Maps API"""
    @staticmethod
    def create_location() -> Response:
        post_url: str = f"{BASE_URL}{POST_RESOURCE}?{KEY}"
        post_body = {
            "location": {"lat": -38.383494, "lng": 33.427362},
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": ["shoe park", "shop"],
            "website": "http://google.com",
            "language": "French-IN"
        }

        with allure.step("Создание локации"):
            logger.info(f"POST URL: {post_url}")
            logger.info(f"POST Body: {post_body}")
            post_result = HttpMethods.post(post_url, post_body)
            logger.info(f"Response: {post_result.text}")
            return post_result

    @staticmethod
    def get_location(place_id) -> Response:
        get_url = f"{BASE_URL}{GET_RESOURCE}?{KEY}&place_id={place_id}"

        with allure.step(f"Получение локации place_id={place_id}"):
            logger.info(f"GET URL: {get_url}")
            get_result = HttpMethods.get(get_url)
            logger.info(f"Response: {get_result.text}")
            return get_result

    @staticmethod
    def put_location(place_id) -> Response:
        put_url = f"{BASE_URL}{PUT_RESOURCE}?{KEY}"
        put_body = {"place_id": place_id, "address": "100 Lenina street, RU", "key": "qaclick123"}

        with allure.step(f"Изменение адреса локации place_id={place_id}"):
            logger.info(f"PUT URL: {put_url}")
            logger.info(f"PUT Body: {put_body}")
            put_result = HttpMethods.put(put_url, put_body)
            logger.info(f"Response: {put_result.text}")
            return put_result

    @staticmethod
    def delete_location(place_id) -> Response:
        delete_url = f"{BASE_URL}{DELETE_RESOURCE}?{KEY}"
        delete_body = {"place_id": place_id}

        with allure.step(f"Удаление локации place_id={place_id}"):
            logger.info(f"DELETE URL: {delete_url}")
            logger.info(f"DELETE Body: {delete_body}")
            delete_result = HttpMethods.delete(delete_url, delete_body)
            logger.info(f"Response: {delete_result.text}")
            return delete_result