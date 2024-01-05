import requests
import json
import jsonschema
from pydantic import ValidationError

from src.Utils import *
import logging


class Method_error(Exception):
    pass


logging.basicConfig(level=logging.INFO)


class BaseModelRequest:
    """
    Этот код представляет класс BaseModelRequest, который является базовым классом для выполнения HTTP-запросов и их валидации. Ниже представлено описание методов и их использование.

    __init__(self, endpoint)
    Конструктор класса, принимающий endpoint в качестве аргумента. Устанавливает базовый URL baseurl для всех запросов и сохраняет переданный endpoint.

    make_request(self, method, params=None, headers=None, body=None, logining_errors=False)
    Метод для выполнения HTTP-запроса. Принимает следующие параметры:

    method (str): HTTP-метод запроса.
    params (dict, optional): Параметры запроса.
    headers (dict, optional): Заголовки запроса.
    body (dict, optional): Тело запроса в формате JSON.
    logining_errors (bool, optional): Флаг для вывода ошибок в консоль.
    Возвращает объект requests.Response после успешного выполнения запроса. Если произошла ошибка и logining_errors установлен в True, поднимает исключение requests.exceptions.RequestException.

    asset_validate_jsonschema(self, jsonfile, schema, logining_errors=False)
    Метод для проверки соответствия JSON-файла заданной JSON-схеме. Принимает:

    jsonfile (dict or list): JSON-файл или список JSON-файлов для валидации.
    schema (dict): JSON-схема, с которой сравнивается JSON-файл.
    logining_errors (bool, optional): Флаг для вывода ошибок в консоль.
    Если произошла ошибка валидации и logining_errors установлен в True, будет вызвано исключение ValidationError.

    assert_validate_status_code(self, actual_code, expected_code, logining_errors=False)
    Метод для проверки соответствия фактического HTTP-статус кода ожидаемому. Принимает:

    actual_code (int): Фактический HTTP-статус код, полученный после выполнения запроса.
    expected_code (int): Ожидаемый HTTP-статус код.
    logining_errors (bool, optional): Флаг для вывода ошибок в консоль.
    Если произошла ошибка и logining_errors установлен в True, будет вызвано исключение AssertionError.

    log_error(self, error_message)
    Метод для логирования ошибок с использованием модуля logging.

    validate_pydantic(self, json_data, obj, model_resposne, parametr=None)
    Метод для валидации данных с использованием Pydantic модели. Принимает:

    json_data (dict): JSON-данные, подлежащие валидации.
    obj (str or list): Наименование поля (строка) или список наименований полей для валидации.
    model_resposne (PydanticModel): Экземпляр Pydantic-модели для валидации данных.
    parametr (str or list, optional): Ожидаемое значение (строка или список значений) для валидации поля.
    Если произошла ошибка валидации, будет вызвано исключение ValidationError.
    """

    def __init__(self, endpoint):
        self.baseurl = "https://qauto.forstudy.space/api"
        self.endpoint = endpoint

    def make_request(self, method, params=None, headers=None, body=None, logining_errors=False):
        """
           Выполнение HTTP-запроса к заданному эндпоинту с использованием указанного метода.

           Параметры:
           - method (str): HTTP-метод запроса. Должен быть одним из ["get", "post", "put", "delete"].
           - params (dict, optional): Параметры запроса. По умолчанию, None.
           - headers (dict, optional): Заголовки запроса. По умолчанию, None.
           - body (dict, optional): Тело запроса в формате JSON. По умолчанию, None.
           - logining_errors (bool, optional): Флаг для вывода ошибок в консоль. По умолчанию, ошибки не выводятся.

           Возвращает:
           - requests.Response: Объект Response после успешного выполнения запроса.
           - None: В случае ошибки, если `logining_errors` установлен в False.
           - requests.exceptions.RequestException: В случае ошибки, если `logining_errors` установлен в True.

           Выполняет HTTP-запрос к эндпоинту, объединяя базовый URL и путь эндпоинта.
           Проверяет корректность указанного HTTP-метода и поднимает исключение Method_error в случае ошибки.
           После успешного выполнения запроса возвращает объект Response с содержимым ответа.
           В случае ошибки выводит сообщение об ошибке и, при необходимости, поднимает исключение RequestException,
           если `logining_errors` установлен в True.

           Пример использования:
           ```python
           response = make_request("get", params={"param1": "value1"}, headers={"Authorization": "Bearer token"})
           print(response.json())
           ```

           Пример с использованием обработки ошибок:
           ```python
           try:
               response = make_request("post", body={"key": "value"}, logining_errors=True)
           except requests.exceptions.RequestException as e:
               print(f"Error in making request: {e}")
           ```
           """
        methods = ["get", "post", "put", "delete"]
        if method.lower() not in methods:
            raise Method_error("This method is incorrect")
        try:
            endpoint = f"{self.baseurl}{self.endpoint}"
            response = getattr(requests, method.lower())(endpoint, headers=headers,
                                                         params=params, json=body)
            response.raise_for_status()
            if not logining_errors:
                print(f"Response content: {response.content.decode('utf-8')}")
                print(f"Error is not  making request: {endpoint}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error in making request: {e}")
            if e.response.status_code >= 400:
                print(f"Response content: {response.content.decode('utf-8')}")
            if not logining_errors:
                return response
            else:
                raise e

    @staticmethod
    def asset_validate_jsonschema(jsonfile, schema, logining_errors=False):
        """
           Проверка соответствия JSON-файла заданной JSON-схеме.

           Параметры:
           - jsonfile (dict or list): JSON-файл или список JSON-файлов для валидации.
           - schema (dict): JSON-схема, с которой сравнивается JSON-файл.
           - logining_errors (bool, optional): Флаг для вывода ошибок в консоль. По умолчанию, ошибки не выводятся.

           Возвращает:
           - None: В случае успешной валидации не возвращает значения.
           - Exception: Если произошла ошибка валидации и `logining_errors` установлен в True, будет вызвано исключение ValidationError.

           Проверяет переданный JSON-файл или список JSON-файлов на соответствие заданной JSON-схеме.
           В случае успешной валидации выводит сообщение об успешной валидации.
           В случае ошибки валидации выводит сообщение об ошибке валидации и, при необходимости,
           поднимает исключение ValidationError, если `logining_errors` установлен в False.

           Пример использования:
           ```python
           asset_validate_jsonschema(json_data, my_json_schema)
           ```

           Пример с использованием списка JSON-файлов:
           ```python
           asset_validate_jsonschema([json_data1, json_data2], my_json_schema, logining_errors=True)
           ```

           Параметр `logining_errors` управляет выводом ошибок в консоль и может быть полезен, например,
           в сценариях тестирования, где нужно избежать завершения теста из-за ошибки валидации.
           """
        Shema_validate_in_function = VALIDATION_SCHEMA_OK
        extention = None
        if isinstance(jsonfile, list):
            for value in jsonfile:
                try:
                    jsonschema.validate(instance=value, schema=schema)
                except jsonschema.exceptions.ValidationError as e:
                    print(e)
                    extention = e
                    Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        else:
            try:
                jsonschema.validate(instance=jsonfile, schema=schema)
            except jsonschema.exceptions.ValidationError as e:
                print(e.json())
                extention = e
                Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        if not logining_errors:
            assert Shema_validate_in_function == VALIDATION_SCHEMA_OK
        else:
            raise extention

    @staticmethod
    def assert_validate_status_code(actual_code, expected_code, logining_errors=False):
        """
            Проверка соответствия фактического HTTP-статус кода ожидаемому.

            Параметры:
            - actual_code (int): Фактический HTTP-статус код, полученный после выполнения запроса.
            - expected_code (int): Ожидаемый HTTP-статус код.
            - logining_errors (bool, optional): Флаг для вывода ошибок в консоль. По умолчанию, ошибки не выводятся.

            Возвращает:
            - None: В случае успешной проверки не возвращает значения.
            - AssertionError: В случае ошибки, если `logining_errors` установлен в False.

            Проверяет фактический HTTP-статус код на соответствие ожидаемому.
            В случае успешной проверки ничего не возвращает.
            В случае ошибки выводит сообщение об ошибке и поднимает исключение AssertionError,
            если `logining_errors` установлен в False.

            Пример использования:
            ```python
            assert_validate_status_code(response.status_code, 200)
            ```

            Пример с использованием обработки ошибок:
            ```python
            try:
                assert_validate_status_code(response.status_code, 404, logining_errors=True)
            except AssertionError as e:
                print(f"Error in validating status code: {e}")
            ```
            """
        Shema_validate_in_function = VALIDATION_SCHEMA_OK
        if actual_code != expected_code:
            Shema_validate_in_function = VALIDATION_SCHEMA_FAIL
        assert Shema_validate_in_function == VALIDATION_SCHEMA_OK

    def log_error(self, error_message):
        logging.error(error_message)

    @staticmethod
    def validate_pydantic(json_data, obj, model_resposne, parametr=None):
        """
    Валидация данных с использованием Pydantic модели.

    Параметры:
    - json_data (dict): JSON-данные, подлежащие валидации.
    - obj (str or list): Наименование поля (строка) или список наименований полей для валидации.
    - model_resposne (PydanticModel): Экземпляр Pydantic-модели для валидации данных.
    - parametr (str or list, optional): Ожидаемое значение (строка или список значений) для валидации поля.

    Возвращает:
    - None: В случае успешной валидации не возвращает значения. В случае ошибки вызывает исключение ValidationError.

    Проверяет переданные JSON-данные на соответствие Pydantic-модели и, при необходимости, проверяет значения поля или полей
    на соответствие ожидаемым значениям. В случае успешной валидации выводит сообщение "Данные валидные".
    В случае ошибки валидации выводит сообщение "Ошибка валидации данных" и поднимает исключение ValidationError.

    Пример использования:
    ```python
    validate_pydantic(json_data, "field_name", MyPydanticModel, "expected_value")
    ```

    Пример с использованием списка полей:
    ```python
    validate_pydantic(json_data, ["field1", "field2"], MyPydanticModel, ["value1", "value2"])
    ```

    Параметр `parametr` используется для сравнения значений полей. Если не передан, выполняется стандартная валидация.
    """
        Status_validation = None
        try:
            model_resposne.model_validate(json_data)
            print("Данные валидные")
            if parametr is not None:
                if (isinstance(parametr, list) and isinstance(obj, list)) and len(parametr) == len(obj):
                    for key, value in zip(parametr, obj):
                        if json_data["data"].get(key, "Error") != value:
                            raise ValidationError("Ошибка валидации данных")
                if json_data["data"].get(obj, "Error") != parametr:
                    raise ValidationError("Ошибка валидации данных")
            elif json_data["data"].get(obj, "Error") != "Test":
                raise ValidationError("Ошибка валидации данных")
            Status_validation = VALIDATION_SCHEMA_OK
        except (Exception, ValidationError) as e:
            print(f"Ошибка валидации данных: {e}")
            Status_validation = VALIDATION_SCHEMA_FAIL
        assert Status_validation == VALIDATION_SCHEMA_OK
