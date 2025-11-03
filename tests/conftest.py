import pytest
from requests import Response

from utils.api import RsMapsApi
from utils.checks import Checking


@pytest.fixture
def created_location():
    """Фикстура для создания тестовой локации"""