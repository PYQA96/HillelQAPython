import jsonschema
from pydantic import ValidationError
from src.UTILS import *
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

    # @allure.step("Validate pydantic shema")
    # def validate_pydantic(self, obj, model_schema, parametr=None, response=None,massivkey=None):
    #
    #     if response is None:
    #         response = self.resposnses.json()
    #     erros_raise = None
    #     Status_validation = None
    #     try:
    #         model_schema.model_validate(response)
    #
    #         if massivkey != "data" and response[massivkey] == obj:
    #             Status_validation = VALIDATION_SCHEMA_OK
    #         elif massivkey != 'data' and response[massivkey] != obj:
    #             raise ValidationError("Ошибка валидации данных")
    #         elif parametr is not None:
    #             if (isinstance(parametr, list) and isinstance(obj, list)) and len(parametr) == len(obj):
    #                 for key, value in zip(obj, parametr):
    #                     if response[massivkey].get(key, "Error") != value:
    #                         raise ValidationError("Ошибка валидации данных")
    #             elif response[massivkey].get(obj, "Error") != parametr:
    #                 raise ValidationError("Ошибка валидации данных")
    #         elif response[massivkey].get(obj, "Error") != "Test":
    #             raise ValidationError("Ошибка валидации данных")
    #         logging.info("Данные валидные")
    #     except   ValidationError as e:
    #         erros_raise = e
    #         print(e)
    #         Status_validation = VALIDATION_SCHEMA_FAIL
    #     if Status_validation == VALIDATION_SCHEMA_FAIL:
    #         logging.error(f"Ошибка валидации : {erros_raise}")
    #     assert Status_validation == VALIDATION_SCHEMA_OK

    @allure.step("Validate pydantic schema")
    def validate_pydantic(self, obj, model_schema, parametr=None, response=None, massivkey=None):
        if response is None:
            response = self.resposnses.json()
        Status_validation = VALIDATION_SCHEMA_OK
        erorr_raise=None
        if response is None:
            response = self.resposnses.json()

        try:
            model_schema.model_validate(response)

            if massivkey != "data":
                if response.get(massivkey) == obj:
                    logging.info("Данные валидные")
                else:
                    raise ErrorValidationParametr("Ошибка валидации данных")

            elif parametr is not None:
                if isinstance(parametr, list) and isinstance(obj, list) and len(parametr) == len(obj):
                    for key, value in zip(obj, parametr):
                        if response[massivkey].get(key) != value:
                            raise ErrorValidationParametr("Ошибка валидации данных")
                elif response[massivkey].get(obj) != parametr:
                    raise ErrorValidationParametr("Ошибка валидации данных")
            else:
                if response[massivkey].get(obj) != "Test":
                    raise ErrorValidationParametr("Ошибка валидации данных")

            logging.info("Данные валидные")

        except (ErrorValidationParametr,ValidationError) as e:
            erorr_raise = e
            logging.error(f"Ошибка валидации: {e}")
            Status_validation = VALIDATION_SCHEMA_FAIL
        assert Status_validation == VALIDATION_SCHEMA_OK,f"Ошибка валидации: {erorr_raise}"