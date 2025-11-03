import pytest
from requests import Response

from utils.api import RsMapsApi
from utils.checks import Checking


@pytest.fixture
def created_location():
    """Фикстура для создания локации и возвращения её place_id"""
    print("\nPOST: создание локации (предусловие)")
    post_result: Response = RsMapsApi.create_location()
    check_post_result = post_result.json()
    place_id = check_post_result.get("place_id")
    Checking.check_status_code(post_result, 200)
    Checking.check_json_token(post_result,
                              ['status', 'place_id', 'scope', 'reference', 'id'])
    yield place_id
