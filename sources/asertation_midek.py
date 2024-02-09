import jsonschema
from pydantic import ValidationError
from sources.utils import *
import logging
import allure

class ErrorValidationParametr(Exception):
    pass

class Assertation_model_methods:

    def __init__(self, resposnse):
        self.resposnses = resposnse
        logging.info('resposnse: url={}'.format(f"{self.resposnses}"))


    @allure.step("Validate json shema")
    def asset_validate_jsonschema(self, schema, response=None, logining_errors=False):
        if schema is None and response is None:
            logging.info("ропуск теста Validate json shema, данные для теста не зданы")
            return self.resposnses
        if response is None:
            response = self.resposnses.json()
        Shema_validate_in_function = VALIDATION_SCHEMA_OK
        extention = None
        if isinstance(response, list):
            for value in response:
                try:
                    jsonschema.validate(instance=value, schema=schema)
                except jsonschema.exceptions.ValidationError as e:
                    logging.info(e)
                    extention = e
                    Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        else:
            try:
                jsonschema.validate(instance=response, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                logging.info(e.json())
                extention = e
                Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        if not logining_errors:
            logging.info(f"Validation Pased")
            assert Shema_validate_in_function == VALIDATION_SCHEMA_OK

        else:
            raise extention

    @allure.step("Validate status code")
    def assert_validate_status_code(self, expected_code, actual_code=None, logining_errors=False):
        if expected_code is None and actual_code is None:
            logging.info("пропуск теста Validate status code, данные не заданы")
            return self
        if actual_code is None:
            actual_code = self.resposnses.status_code
        erros_raise = None
        Shema_validate_in_function = VALIDATION_SCHEMA_OK
        try:
            if actual_code != expected_code:
                Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        except Exception as e:
            erros_raise = e
        if not logining_errors:
            assert Shema_validate_in_function == VALIDATION_SCHEMA_OK
            return self
        else:
            return erros_raise


    # @allure.step("Validate pydantic schema")
    # def validate_pydantic(self, key, model_schema, value=None, response=None, massivkey=None):
    #     if response is None:
    #         response = self.resposnses.json()
    #     Status_validation = VALIDATION_SCHEMA_OK
    #     erorr_raise=None
    #     if response is None:
    #         response = self.resposnses.json()
    #
    #     try:
    #         model_schema.model_validate(response)
    #
    #         if massivkey != "data":
    #             if response.get(massivkey) == key:
    #                 logging.info("Данные валидные")
    #             else:
    #                 raise ErrorValidationParametr("Ошибка валидации данных")
    #
    #         elif value is not None:
    #             if isinstance(value, list) and isinstance(key, list) and len(value) == len(key):
    #                 for key, value in zip(key, value):
    #                     if response[massivkey].get(key) != value:
    #                         raise ErrorValidationParametr("Ошибка валидации данных")
    #             elif response[massivkey].get(key) != value:
    #                 raise ErrorValidationParametr("Ошибка валидации данных")
    #         else:
    #             if response[massivkey].get(key) != "Test":
    #                 raise ErrorValidationParametr("Ошибка валидации данных")
    #
    #         logging.info("Данные валидные")
    #
    #     except (ErrorValidationParametr,ValidationError) as e:
    #         erorr_raise = e
    #         logging.error(f"Ошибка валидации: {e}")
    #         Status_validation = VALIDATION_SCHEMA_FAIL
    #     assert Status_validation == VALIDATION_SCHEMA_OK,f"Ошибка валидации: {erorr_raise}"
    @allure.step("Validate pydantic schema")
    def validate_pydantic(self, model_schema, response=None,):
        if response is None:
            response = self.resposnses.json()
        Status_validation = VALIDATION_SCHEMA_OK
        erorr_raise = None

        try:
            model_schema.model_validate(response)

        except  ValidationError as e:
            erorr_raise = e
            logging.error(f"Ошибка валидации: {e}")
            Status_validation = VALIDATION_SCHEMA_FAIL
        assert Status_validation == VALIDATION_SCHEMA_OK, f"Ошибка валидации: {erorr_raise}"

    @allure.step("params_equal")
    def params_equal(self, key=None, value=None, massivkey=None):

        response = self.resposnses.json() if not isinstance(self.resposnses, dict) else self.resposnses
        if key is None and value is None:
            logging.info("Пропуск теста params_equal, не заданы параметры для проверки")
            return self
        Status_validation = VALIDATION_SCHEMA_OK
        erorr_raise = None
        try:
            if isinstance(key, list) and isinstance(value, list):
                for key, val in zip(key, value):
                    if massivkey is not None:
                        if response[massivkey].get(key) != val:
                            logging.error(f"Ошибка валидации данных, в массиве {massivkey} значение  {response[massivkey].get(key)} не равен  проверочному значению {val}")
                            raise ErrorValidationParametr(
                                f"Ошибка валидации данных, в массиве {massivkey} значение  {response[massivkey].get(key)} не равен  проверочному значению {val}")
                    elif response.get(key) != val:
                        logging.error(
                            f"Ошибка валидации данных,  {response.get(key)} не равен значение {val}, в строке")
                        raise ErrorValidationParametr(
                            f"Ошибка валидации данных,  {response.get(key)} не равен значение {val}, в строке")
            else:
                if massivkey is not None:
                    if response[massivkey].get(key) != value:
                        logging.error(
                            f"Ошибка валидации данных, ключ {key} не равен значение {value}, в масиве двумерном , с ключем {massivkey}")
                        raise ErrorValidationParametr(
                            f"Ошибка валидации данных, ключ {key} не равен значение {value}, в масиве двумерном , с ключем {massivkey}")
                elif response.get(key) != value:
                    logging.error(f"Ошибка валидации данных,  {response.get(key)} не равен значение {value}, в строке с ключем {massivkey}")
                    raise ErrorValidationParametr(
                        f"Ошибка валидации данных,  {response.get(key)} не равен значение {value}, в строке с ключем {massivkey}")
        except ErrorValidationParametr as e:
            logging.error(f"{e}")
            erorr_raise = e
            Status_validation = VALIDATION_SCHEMA_FAIL
        assert Status_validation == VALIDATION_SCHEMA_OK, f"Ошибка валидации: {erorr_raise}"
        return self


    # def params_equal(self,  key=None, value=None, massivkey=None):
    #
    #
    #     response = self.resposnses.json() if not isinstance(self.resposnses,dict) else self.resposnses
    #     if key == None and value == None:
    #         logging.info(f"Пропуск теста params_equal ,не заданы параметры для проверки ")
    #         return self
    #     Status_validation = VALIDATION_SCHEMA_OK
    #     erorr_raise = None
    #     try:
    #         if massivkey is None:
    #             if isinstance(key, list) and isinstance(value, list):
    #                 for key,value in zip(key, value):
    #                     if response.get(key) != value:
    #                         raise ErrorValidationParametr(f"Ошибка валидации данных, ключ {key} не равен значение {value}, в масиве")
    #             elif response.get(key) != value:
    #                 raise ErrorValidationParametr(
    #                     f"Ошибка валидации данных, ключ {key} не равен значение {value}, в строке")
    #         else:
    #             if isinstance(key, list) and isinstance(value, list):
    #                 for key, value in zip(key, value):
    #                     if response[massivkey].get(key) != value:
    #                         raise ErrorValidationParametr(
    #                             f"Ошибка валидации данных, ключ {key} не равен значение {value}, в масиве")
    #             elif response.get(massivkey).get(key) != value:
    #                 raise ErrorValidationParametr(
    #                     f"Ошибка валидации данных, ключ {key} не равен значение {value}, в строке")
    #     except ErrorValidationParametr as e:
    #         logging.error(f"Ошибка валидации: {e}")
    #         Status_validation = VALIDATION_SCHEMA_FAIL
    #     assert Status_validation == VALIDATION_SCHEMA_OK, f"Ошибка валидации: {erorr_raise}"
    #     return self