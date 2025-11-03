from requests import Response

from utils.api import RsMapsApi


class TestCreateLocation:
    def test_create_location(self):
        print("Метод POST: создание новой локации")
        post_result: Response = RsMapsApi.create_location