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
    def create_location():
        post_url: str = f"{BASE_URL}{POST_RESOURCE}?{KEY}"
        logger.info(f"Url запроса: {post_url}")
        post_body: dict[str, list[str] | str | int | dict[str, float]] = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        logger.info(f"Тело запроса: {post_body}")

        post_result: Response = HttpMethods.post(post_url, post_body)
        logger.info(f"Заголовки ответа: {post_result.headers}")
        logger.info(f"Тело ответа: {post_result.text}")
        logger.info(f"Статус-код ответа: {post_result.status_code}")
        return post_result

    @staticmethod
    def get_location(place_id):
        get_url: str = f"{BASE_URL}{GET_RESOURCE}?{KEY}&place_id={place_id}"
        logger.info(f"Url запроса: {get_url}")
        get_result: Response = HttpMethods.get(get_url)
        logger.info(f"Заголовки ответа: {get_result.headers}")
        logger.info(f"Тело ответа: {get_result.text}")
        logger.info(f"Статус-код ответа: {get_result.status_code}")
        return get_result

    @staticmethod
    def put_location(place_id):
        put_url: str = f"{BASE_URL}{PUT_RESOURCE}?{KEY}"
        put_body: dict[str, list[str] | str | int | dict[str, float]] = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        logger.info(f"Url запроса: {put_url}")
        logger.info(f"Тело запроса: {put_body}")
        put_result: Response = HttpMethods.put(put_url, put_body)
        logger.info(f"Заголовки ответа: {put_result.headers}")
        logger.info(f"Тело ответа: {put_result.text}")
        logger.info(f"Статус-код ответа: {put_result.status_code}")
        return put_result

    @staticmethod
    def delete_location(place_id):
        delete_url: str = f"{BASE_URL}{DELETE_RESOURCE}?{KEY}"
        delete_body: dict[str, list[str] | str | int | dict[str, float]] = {
            "place_id": place_id
        }
        logger.info(f"Url запроса: {delete_url}")
        logger.info(f"Тело запроса: {delete_body}")
        delete_result: Response = HttpMethods.delete(delete_url, delete_body)
        logger.info(f"Заголовки ответа: {delete_result.headers}")
        logger.info(f"Тело ответа: {delete_result.text}")
        logger.info(f"Статус-код ответа: {delete_result.status_code}")
        return delete_result