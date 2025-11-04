from utils.api import RsMapsApi
from utils.checks import Checking
from requests import Response
from logger_config import logger
import allure



@allure.epic("RsMapsApi: TestLocationLifecycle")
class TestLocationLifecycle:
    """Проверка жизненного цикла локации: создание -> чтение -> обновление -> удаление"""
    def test_location_lifecycle(self, created_location):
        place_id = created_location
        logger.info("GET: проверка, создалась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [
            'location', 'accuracy', 'name', 'phone_number',
            'address', 'types', 'website', 'language'
        ])
        Checking.check_json_filds(get_result, "status", "OK")

        logger.info("PUT: изменение адреса локации")
        put_result: Response = RsMapsApi.put_location(place_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_token(put_result, ["msg"])
        Checking.check_json_filds(put_result, 'msg', 'Address successfully updated')

        logger.info("GET: проверка, изменился ли адрес локации")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [['location', 'name', 'address']])
        Checking.check_json_filds(get_result, 'address', '100 Lenina street, RU')

        logger.info("DELETE: удаление локации")
        delete_result: Response = RsMapsApi.delete_location(place_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ["status"])
        Checking.check_json_filds(delete_result, 'status', 'OK')

        logger.info("GET: проверка, удалилась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_token(get_result, ["msg"])
        Checking.check_json_filds(get_result, 'msg', 'Get operation failed')

        logger.success("Тестирование жизненного цикла локации прошло успешно!")



@allure.epic("RsMapsApi: TestLocationNegative")
class TestLocationNegative:
    """Негативное тестирование"""
    def test_get_location_without_place_id(self):
        logger.info("GET: попытка получить локацию с пустой строкой вместо place_id")
        get_result = RsMapsApi.get_location("")
        Checking.check_status_code(get_result, 404)
        Checking.check_json_filds(get_result, 'msg', 'Get operation failed')
        logger.success("Негативное тестирование на получение локации с пустой строкой прошло успешно!")

    def test_update_location_without_place_id(self):
        logger.info("PUT: попытка обновить локацию с пустой строкой вместо place_id")
        update_result = RsMapsApi.put_location("")
        Checking.check_status_code(update_result, 404)
        logger.success("Негативное тестирование на изменение локации с пустой строкой прошло успешно!")

    def test_delete_location_without_place_id(self):
        logger.info("DELETE: попытка удалить локацию с пустой строкой вместо place_id")
        delete_result = RsMapsApi.delete_location("")
        Checking.check_status_code(delete_result, 404)
        logger.success("Негативное тестирование на удаление локации с пустой строкой прошло успешно!")

    def test_get_nonexistent_location(self):
        fake_place_id = "0000000000"
        logger.info(f"GET: попытка получить несуществующую локацию ({fake_place_id})")
        get_result: Response = RsMapsApi.get_location(fake_place_id)
        Checking.check_status_code(get_result, 404)
        logger.success("Негативное тестирование на получение несуществующей локации прошло успешно!")

    def test_delete_nonexistent_location(self):
        fake_place_id = "0000000000"
        logger.info(f"DELETE: попытка удалить несуществующую локацию ({fake_place_id})")
        delete_result: Response = RsMapsApi.delete_location(fake_place_id)
        Checking.check_status_code(delete_result, 404)
        logger.success("Негативное тестирование на удаление несуществующей локации прошло успешно!")



@allure.epic("RsMapsApi: TestLocationLocal")
class TestLocationLocal:
    """Тестирование отдельных операций с локацией"""
    def test_only_create_location(self, created_location):
        place_id = created_location
        logger.info("GET: проверка, создалась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [
            'location', 'accuracy', 'name', 'phone_number',
            'address', 'types', 'website', 'language'
        ])
        Checking.check_json_filds(get_result, "status", "OK")
        logger.success("Тестирование только создания локации прошло успешно!")

    def test_only_get_location(self, created_location):
        place_id = created_location
        logger.info(f"GET: проверка получения локации по существующему place_id={place_id}")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [['location', 'name', 'address']])
        Checking.check_json_filds(get_result, "status", "OK")
        logger.success("Тестирование только получения локации прошло успешно!")

    def test_only_change_location(self, created_location):
        place_id = created_location
        logger.info(f"PUT: изменение адреса локации place_id={place_id}")
        put_result: Response = RsMapsApi.put_location(place_id)
        Checking.check_status_code(put_result, 200)
        Checking.check_json_token(put_result, ["msg"])
        Checking.check_json_filds(put_result, 'msg', 'Address successfully updated')

        logger.info("GET: проверка, изменился ли адрес локации")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 200)
        Checking.check_json_token(get_result, [['location', 'name', 'address']])
        logger.success("Тестирование только изменения локации прошло успешно!")

    def test_only_delete_location(self, created_location):
        place_id = created_location
        logger.info(f"DELETE: удаление локации place_id={place_id}")
        delete_result: Response = RsMapsApi.delete_location(place_id)
        Checking.check_status_code(delete_result, 200)
        Checking.check_json_token(delete_result, ["status"])
        Checking.check_json_filds(delete_result, 'status', 'OK')

        logger.info("GET: проверка, удалилась ли локация")
        get_result: Response = RsMapsApi.get_location(place_id)
        Checking.check_status_code(get_result, 404)
        Checking.check_json_token(get_result, ["msg"])
        Checking.check_json_filds(get_result, 'msg', 'Get operation failed')
        logger.success("Тестирование только удаления локации прошло успешно!")
