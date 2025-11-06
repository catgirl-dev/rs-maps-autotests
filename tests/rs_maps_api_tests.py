from allure_commons.types import Severity

from utils.rs_maps_api import RsMapsApi
from utils.checks import Checking
from requests import Response
from logger_config import logger
import allure



@allure.parent_suite("RsMaps API")
@allure.feature("Жизненный цикл локации")
class TestLocationLifecycle:
    """Проверка жизненного цикла локации: создание → чтение → обновление → удаление"""
    @allure.severity(Severity.CRITICAL)
    @allure.title("Полный цикл: создание, обновление и удаление локации")
    def test_location_full_lifecycle(self, created_location):
        place_id = created_location

        with allure.step("GET: проверка, что локация успешно создана"):
            logger.info(f"GET запрос локации place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [
                'location', 'accuracy', 'name', 'phone_number',
                'address', 'types', 'website', 'language'
            ])
            allure.attach(get_result.text, name="GET Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("PUT: изменение адреса локации"):
            logger.info(f"PUT запрос изменения адреса локации place_id={place_id}")
            put_result: Response = RsMapsApi.put_location(place_id)
            Checking.check_status_code(put_result, 200)
            Checking.check_json_token(put_result, ["msg"])
            Checking.check_json_fields(put_result, 'msg', 'Address successfully updated')
            allure.attach(put_result.text, name="PUT Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка, что адрес успешно обновлён"):
            logger.info(f"GET запрос локации после обновления place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            Checking.check_json_fields(get_result, 'address', '100 Lenina street, RU')
            allure.attach(get_result.text, name="GET after PUT Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("DELETE: удаление локации"):
            logger.info(f"DELETE запрос удаления локации place_id={place_id}")
            delete_result: Response = RsMapsApi.delete_location(place_id)
            Checking.check_status_code(delete_result, 200)
            Checking.check_json_token(delete_result, ["status"])
            Checking.check_json_fields(delete_result, 'status', 'OK')
            allure.attach(delete_result.text, name="DELETE Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка, что локация действительно удалена"):
            logger.info(f"GET запрос после удаления локации place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 404)
            Checking.check_json_token(get_result, ["msg"])
            Checking.check_json_fields(
                get_result,
                "msg",
                "Get operation failed, looks like place_id  doesn't exists"
            )
            allure.attach(get_result.text, name="GET after DELETE Response",
                          attachment_type=allure.attachment_type.JSON)

        logger.success("Жизненный цикл локации успешно протестирован!")



@allure.parent_suite("RsMaps API")
@allure.feature("Негативные тесты API локаций")
class TestLocationNegative:
    """Проверка поведения API при некорректных входных данных"""
    @allure.severity(Severity.NORMAL)
    @allure.title("GET: получение локации с пустым place_id ('')")
    def test_get_location_with_empty_place_id(self):
        with allure.step("GET: попытка получить локацию с пустым place_id('')"):
            logger.info("GET: попытка получить локацию с пустым place_id('')")
            get_result = RsMapsApi.get_location("")
            Checking.check_status_code(get_result, 404)
            Checking.check_json_fields(get_result, 'msg',
                                      "Get operation failed, looks like place_id  doesn't exists")
            allure.attach(get_result.text, name="GET: попытка получить локацию с пустым place_id('')",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Проверка GET с пустым place_id('') прошла успешно!")

    @allure.severity(Severity.NORMAL)
    @allure.title("PUT: обновление локации с пустым place_id ('')")
    def test_update_location_with_empty_place_id(self):
        with allure.step("PUT запрос с пустым place_id ('')"):
            logger.info("PUT запрос с пустым place_id ('')")
            put_result = RsMapsApi.put_location("")
            Checking.check_status_code(put_result, 404)
            allure.attach(put_result.text, name="PUT запрос с пустым place_id ('')",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Проверка PUT с пустым place_id прошла успешно!")

    @allure.severity(Severity.NORMAL)
    @allure.title("DELETE: удаление локации с пустым place_id ('')")
    def test_delete_location_with_empty_place_id(self):
        with allure.step("DELETE: удаление локации с пустым place_id ('')"):
            logger.info("DELETE: удаление локации с пустым place_id ('')")
            delete_result: Response = RsMapsApi.delete_location("")
            Checking.check_status_code(delete_result, 404)
            allure.attach(delete_result.text, name="DELETE: удаление локации с пустым place_id ('')",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Проверка DELETE с пустым place_id прошла успешно!")

    @allure.severity(Severity.NORMAL)
    @allure.title("GET: получение несуществующей локации (place_id='0000000000')")
    def test_get_location_with_nonexistent_id(self):
        fake_place_id: str = "0000000000"
        with allure.step(f"GET запрос несуществующей локации place_id={fake_place_id})"):
            logger.info(f"GET запрос несуществующей локации place_id={fake_place_id}")
            get_result: Response = RsMapsApi.get_location(fake_place_id)
            Checking.check_status_code(get_result, 404)
            allure.attach(get_result.text,
                          name=f"GET запрос несуществующей локации place_id={fake_place_id}",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Проверка GET несуществующей локации прошла успешно!")

    @allure.severity(Severity.NORMAL)
    @allure.title("DELETE: удаление несуществующей локации (place_id='0000000000')")
    def test_delete_location_with_nonexistent_id(self):
        fake_place_id = "0000000000"
        with allure.step(f"DELETE: попытка удалить несуществующую локацию ({fake_place_id})"):
            logger.info(f"DELETE запрос несуществующей локации place_id={fake_place_id}")
            delete_result: Response = RsMapsApi.delete_location(fake_place_id)
            Checking.check_status_code(delete_result, 404)
            allure.attach(delete_result.text, name="DELETE Nonexistent Response",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Проверка DELETE несуществующей локации прошла успешно!")




@allure.parent_suite("RsMaps API")
@allure.feature("Позитивное тестирование отдельных операций")
class TestLocationSingleOperation:
    """Проверка отдельных операций: создание, чтение, обновление и удаление"""
    @allure.severity(Severity.CRITICAL)
    @allure.title("Создание локации и проверка результата")
    def test_create_location_only(self, created_location):
        place_id = created_location
        with allure.step("GET: проверка, что локация успешно создана"):
            logger.info(f"GET запрос локации place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [
                'location', 'accuracy', 'name', 'phone_number',
                'address', 'types', 'website', 'language'
            ])
            allure.attach(get_result.text, name="GET Response",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Создание локации проверено успешно!")

    @allure.severity(Severity.CRITICAL)
    @allure.title("Получение существующей локации по place_id")
    def test_get_location_only(self, created_location):
        place_id = created_location
        with allure.step(f"GET: получение данных по place_id={place_id}"):
            logger.info(f"GET запрос локации place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            Checking.check_json_fields(get_result, "status", "OK")
            allure.attach(get_result.text, name="GET Response",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Получение локации проверено успешно!")

    @allure.severity(Severity.CRITICAL)
    @allure.title("Обновление адреса локации и проверка изменений")
    def test_update_location_only(self, created_location):
        place_id = created_location
        with allure.step(f"PUT: изменение адреса локации place_id={place_id}"):
            logger.info(f"PUT запрос изменения адреса локации place_id={place_id}")
            put_result: Response = RsMapsApi.put_location(place_id)
            Checking.check_status_code(put_result, 200)
            Checking.check_json_token(put_result, ["msg"])
            Checking.check_json_fields(put_result, 'msg', 'Address successfully updated')
            allure.attach(put_result.text, name="PUT Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка, что адрес обновился"):
            logger.info(f"GET запрос после обновления адреса place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 200)
            Checking.check_json_token(get_result, [['location', 'name', 'address']])
            allure.attach(get_result.text, name="GET запрос после обновления адреса",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Обновление локации проверено успешно!")

    @allure.severity(Severity.CRITICAL)
    @allure.title("Удаление локации и проверка её удаления")
    def test_delete_location_only(self, created_location):
        place_id = created_location
        with allure.step(f"DELETE: удаление локации place_id={place_id}"):
            logger.info(f"DELETE запрос удаления локации place_id={place_id}")
            delete_result: Response = RsMapsApi.delete_location(place_id)
            Checking.check_status_code(delete_result, 200)
            Checking.check_json_token(delete_result, ["status"])
            Checking.check_json_fields(delete_result, 'status', 'OK')
            allure.attach(delete_result.text, name="DELETE Response",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("GET: проверка, что локация удалена"):
            logger.info(f"GET запрос после удаления локации place_id={place_id}")
            get_result: Response = RsMapsApi.get_location(place_id)
            Checking.check_status_code(get_result, 404)
            Checking.check_json_token(get_result, ["msg"])
            Checking.check_json_fields(
                get_result,
                'msg',
                "Get operation failed, looks like place_id  doesn't exists"
            )
            allure.attach(get_result.text, name="Удаление локации проверено успешно!",
                          attachment_type=allure.attachment_type.JSON)
            logger.success("Удаление локации проверено успешно!")
