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

        with allure.step("GET: проверка, создалась ли локация"):
            logger.info(f"GET location place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [
                'location', 'accuracy', 'name', 'phone_number',
                'address', 'types', 'website', 'language'
            ])
            allure.attach(get_result.text, name="GET Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("PUT: изменение адреса локации"):
            logger.info(f"PUT location place_id={place_id}")
            put_result: Response = RsMapsApi.put_location(place_id)
            Checking.check_status_code(put_result, 200)
            Checking.check_json_token(put_result, ["msg"])
            Checking.check_json_filds(put_result, 'msg', 'Address successfully updated')
            allure.attach(put_result.text, name="PUT Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка изменения адреса"):
            logger.info(f"GET location place_id={place_id} after update")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            Checking.check_json_filds(get_result, 'address', '100 Lenina street, RU')
            allure.attach(get_result.text, name="GET after PUT Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("DELETE: удаление локации"):
            logger.info(f"DELETE location place_id={place_id}")
            delete_result: Response = RsMapsApi.delete_location(place_id)
            Checking.check_status_code(delete_result, 200)
            Checking.check_json_token(delete_result, ["status"])
            Checking.check_json_filds(delete_result, 'status', 'OK')
            allure.attach(delete_result.text, name="DELETE Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка удаления локации"):
            logger.info(f"GET location place_id={place_id} after delete")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 404)
            Checking.check_json_token(get_result, ["msg"])
            Checking.check_json_filds(get_result, "msg",
                                      "Get operation failed, looks like place_id  doesn't exists")
            allure.attach(get_result.text, name="GET after DELETE Response", attachment_type=allure.attachment_type.JSON)

        logger.success("Жизненный цикл локации успешно протестирован!")



@allure.epic("RsMapsApi: TestLocationNegative")
class TestLocationNegative:
    """Негативное тестирование"""
    def test_get_location_without_place_id(self):
        with allure.step("GET: попытка получить локацию с пустой строкой вместо place_id"):
            logger.info("GET location with empty place_id")
            get_result = RsMapsApi.get_location("")
            Checking.check_status_code(get_result, 404)
            Checking.check_json_filds(get_result, 'msg',
                                      "Get operation failed, looks like place_id  doesn't exists")
            allure.attach(get_result.text, name="GET Empty place_id Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Негативное тестирование GET с пустым place_id прошло успешно!")

    def test_update_location_without_place_id(self):
        with allure.step("PUT: попытка обновить локацию с пустой строкой вместо place_id"):
            logger.info("PUT location with empty place_id")
            put_result = RsMapsApi.put_location("")
            Checking.check_status_code(put_result, 404)
            allure.attach(put_result.text, name="PUT Empty place_id Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Негативное тестирование PUT с пустым place_id прошло успешно!")

    def test_delete_location_without_place_id(self):
        with allure.step("DELETE: попытка удалить локацию с пустой строкой вместо place_id"):
            logger.info("DELETE location with empty place_id")
            delete_result = RsMapsApi.delete_location("")
            Checking.check_status_code(delete_result, 404)
            allure.attach(delete_result.text, name="DELETE Empty place_id Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Негативное тестирование DELETE с пустым place_id прошло успешно!")

    def test_get_nonexistent_location(self):
        fake_place_id = "0000000000"
        with allure.step(f"GET: попытка получить несуществующую локацию ({fake_place_id})"):
            logger.info(f"GET location with fake_place_id={fake_place_id}")
            get_result: Response = RsMapsApi.get_location(fake_place_id)
            Checking.check_status_code(get_result, 404)
            allure.attach(get_result.text, name="GET Nonexistent Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Негативное тестирование GET несуществующей локации прошло успешно!")

    def test_delete_nonexistent_location(self):
        fake_place_id = "0000000000"
        with allure.step(f"DELETE: попытка удалить несуществующую локацию ({fake_place_id})"):
            logger.info(f"DELETE location with fake_place_id={fake_place_id}")
            delete_result: Response = RsMapsApi.delete_location(fake_place_id)
            Checking.check_status_code(delete_result, 404)
            allure.attach(delete_result.text, name="DELETE Nonexistent Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Негативное тестирование DELETE несуществующей локации прошло успешно!")



@allure.epic("RsMapsApi: TestLocationLocal")
class TestLocationLocal:
    """Тестирование отдельных операций с локацией"""
    def test_only_create_location(self, created_location):
        place_id = created_location
        with allure.step("GET: проверка создания локации"):
            logger.info(f"GET location place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [
                'location', 'accuracy', 'name', 'phone_number',
                'address', 'types', 'website', 'language'
            ])
            allure.attach(get_result.text, name="GET Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Тестирование только создания локации прошло успешно!")

    def test_only_get_location(self, created_location):
        place_id = created_location
        with allure.step(f"GET: проверка получения локации по place_id={place_id}"):
            logger.info(f"GET location place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            Checking.check_json_filds(get_result, "status", "OK")
            allure.attach(get_result.text, name="GET Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Тестирование только получения локации прошло успешно!")

    def test_only_change_location(self, created_location):
        place_id = created_location
        with allure.step(f"PUT: изменение адреса локации place_id={place_id}"):
            logger.info(f"PUT location place_id={place_id}")
            put_result: Response = RsMapsApi.put_location(place_id)
            Checking.check_status_code(put_result, 200)
            Checking.check_json_token(put_result, ["msg"])
            Checking.check_json_filds(put_result, 'msg', 'Address successfully updated')
            allure.attach(put_result.text, name="PUT Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка изменения адреса"):
            logger.info(f"GET location place_id={place_id} after update")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            allure.attach(get_result.text, name="GET after PUT Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Тестирование только изменения локации прошло успешно!")

    def test_only_delete_location(self, created_location):
        place_id = created_location
        with allure.step(f"DELETE: удаление локации place_id={place_id}"):
            logger.info(f"DELETE location place_id={place_id}")
            delete_result: Response = RsMapsApi.delete_location(place_id)
            Checking.check_status_code(delete_result, 200)
            Checking.check_json_token(delete_result, ["status"])
            Checking.check_json_filds(delete_result, 'status', 'OK')
            allure.attach(delete_result.text, name="DELETE Response", attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка удаления локации"):
            logger.info(f"GET location place_id={place_id} after delete")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 404)
            Checking.check_json_token(get_result, ["msg"])
            Checking.check_json_filds(get_result, 'msg', "Get operation failed, looks like place_id  doesn't exists")
            allure.attach(get_result.text, name="GET after DELETE Response", attachment_type=allure.attachment_type.JSON)
            logger.success("Тестирование только удаления локации прошло успешно!")
