from requests import Response

from utils.http_methods import HttpMethods

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
        print(f"Url: {post_url}")
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

        post_result: Response = HttpMethods.post(post_url, post_body)
        print(f"Body: {post_result.text}")
        print(f"Статус-код: {post_result.status_code}")
        return post_result

    @staticmethod
    def get_location(place_id):
        get_url: str = f"{BASE_URL}{GET_RESOURCE}?{KEY}&place_id={place_id}"
        print(f"Url: {get_url}")
        get_result: Response = HttpMethods.get(get_url)
        print(f"Body: {get_result.text}")
        print(f"Статус-код: {get_result.status_code}")
        return get_result

    @staticmethod
    def put_location(place_id):
        put_url: str = f"{BASE_URL}{PUT_RESOURCE}?{KEY}"
        put_body: dict[str, list[str] | str | int | dict[str, float]] = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(f"Url: {put_url}")
        put_result: Response = HttpMethods.put(put_url, put_body)
        print(f"Body: {put_result.text}")
        print(f"Статус-код: {put_result.status_code}")
        return put_result

    @staticmethod
    def delete_location(place_id):
        delete_url: str = f"{BASE_URL}{DELETE_RESOURCE}?{KEY}"
        delete_body: dict[str, list[str] | str | int | dict[str, float]] = {
            "place_id": place_id
        }
        print(f"Url: {delete_url}")
        delete_result: Response = HttpMethods.delete(delete_url, delete_body)
        print(f"Body: {delete_result.text}")
        print(f"Статус-код: {delete_result.status_code}")
        return delete_result