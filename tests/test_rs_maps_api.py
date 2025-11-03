from requests import Response

from utils.api import RsMapsApi
from utils.checks import Checking

class TestLocationLifecycle:
    """Проверка жизненного цикла локации: создание -> чтение -> обновление -> удаление"""
    def test_location_lifecycle(self, created_location):
        print("\nPOST: создание локации")
        post_result: Response = RsMapsApi.create_location()
        check_post_result = post_result.json()
        place_id = check_post_result.get("place_id")
        Checking.check_status_code(post_result, 200)
        Checking.check_json_token(post_result,
                                  ['status', 'place_id', 'scope', 'reference', 'id'])

        print("\nGET: проверка, создалась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, ['location', 'accuracy', 'name',
                                                'phone_number', 'address', 'types', 'website', 'language'])

        print("\nPUT: изменение адреса локации")
        put_result: Response = RsMapsApi.put_location(place_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_token(put_result, ["msg"])

        print("\nGET: проверка, изменился ли адрес локации")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [['location', 'name', 'address']])

        print("\nDELETE: удаление локации")
        delete_result: Response = RsMapsApi.delete_location(place_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ["status"])

        print("\nGET: проверка, удалилась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_token(get_result, ["msg"])

        print("Тестирование жизненного цикла локации прошло успешно!")
