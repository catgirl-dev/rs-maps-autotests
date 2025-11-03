from requests import Response

from utils.http_methods import HttpMethods

BASE_URL: str = "https://rahulshettyacademy.com"
KEY: str = "key=qaclick123"
GET_RESOURCE: str = "/maps/api/place/get/json"
POST_RESOURCE: str = "/maps/api/place/add/json"
PUT_RESOURCE: str = "/maps/api/place/update/json"
DELETE_RESOURCE: str = "/maps/api/place/delete/json"


class RsMapsApi:
    """ Методы для тестирования RS Maps API """
    @staticmethod
    def create_location():
        post_url: str = f"{BASE_URL}{POST_RESOURCE}?{KEY}"
        print(f"POST url: {post_url}")
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
        print(f"POST text: {post_result.text}")
        return post_result
