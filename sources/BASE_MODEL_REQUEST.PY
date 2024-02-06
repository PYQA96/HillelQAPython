import os
import requests
import logging
import allure
from sources.ASERTATION_MODEL import Assertation_model_methods
from dotenv import load_dotenv


load_dotenv()
URL_ADRESS =os.getenv("URL_ADRESS")
class Method_error(Exception):
    pass


class RequestContext:
    def __init__(self, endpoint, method, schema=None, expected_code=None, response=None, actual_code=None,
                 params=None, headers=None, body=None, log_errors=None, metod_validate=True, key=None,
                 value=None, model_schema=None, ids=None, massivkey=None):
        self.endpoint = endpoint
        self.method = method
        self.schema = schema
        self.expected_code = expected_code
        self.response = response
        self.actual_code = actual_code
        self.params = params
        self.headers = headers
        self.body = body
        self.log_errors = log_errors
        self.metod_validate = metod_validate
        self.key = key
        self.value = value
        self.model_schema = model_schema
        self.ids = ids
        self.massivkey =massivkey


class BaseModelRequest:

    def __init__(self):
        self.baseurl = URL_ADRESS
        logging.info('baseurl: url={}'.format(f"{self.baseurl}"))

    @allure.step("Male create_request")
    def __make_request(self, endpoint, method, params=None, headers=None, body=None, logining_errors=False):
        methods = ['get', 'post', 'put', 'delete', 'head', 'options', 'patch', 'trace']
        if method.lower() not in methods:
            raise Method_error(f"This method is incorrect, method mustbe in {methods}: your method {method}")

        try:

            endpoint = f"{self.baseurl}{endpoint}"
            response = getattr(requests, method.lower())(endpoint, headers=headers, params=params, json=body)
            response.raise_for_status()

            if not logining_errors:
                logging.info(f"Request to {endpoint} was successful.")
                logging.info(f"Response content: {response.content.decode('utf-8')}")

            return response
        except (requests.exceptions.RequestException, Exception) as e:
            if not logining_errors:
                logging.info(f"Error in making create_request to {endpoint}: {e}")
                logging.info(f"Response content: {e.response.content.decode('utf-8')}")

            if not logining_errors:
                logging.error(f"Error in create_request {e}")
                return e.response

            else:
                raise e

    @allure.step("create_request")
    def create_request(self, context):
        allure.attach(context.endpoint, name="Endpoint", attachment_type=allure.attachment_type.TEXT)
        allure.attach(context.method, name="Method", attachment_type=allure.attachment_type.TEXT)
        request = self.__make_request(endpoint=context.endpoint, method=context.method, params=context.params,
                                      headers=context.headers, body=context.body,
                                      logining_errors=context.log_errors)
        request = Assertation_model_methods(request).assert_validate_status_code(actual_code=context.actual_code,
                                                                                 expected_code=context.expected_code).params_equal(
            key=context.key, value=context.value, massivkey=context.massivkey)
        if not context.metod_validate:
            # return request.validate_pydantic(key=context.key, value=context.value,
            #                                  model_schema=context.model_schema,massivkey=context.massivkey)
            return request.validate_pydantic(
                                         model_schema=context.model_schema)
        return request.asset_validate_jsonschema(schema=context.schema, response=context.response)
