import requests
import logging
import allure
from src.ASERTATION_MODEL import Assertation_model_methods


class Method_error(Exception):
    pass


class BaseModelRequest:

    def __init__(self):
        self.baseurl = "https://qauto.forstudy.space/api"
        logging.info('baseurl: url={}'.format(f"{self.baseurl}"))

    @allure.step("Male request")
    def __make_request(self, endpoint, method, params=None, headers=None, body=None, logining_errors=False):
        methods = ["get", "post", "put", "delete"]
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
                logging.info(f"Error in making request to {endpoint}: {e}")
                logging.info(f"Response content: {e.response.content.decode('utf-8')}")

            if not logining_errors:
                logging.error(f"Error in request {e}")
                return e.response

            else:
                raise e

    # @allure.step("Get request {endpoint} {method}")
    # def request(self, endpoint=None, method=None, schema=None, expected_code=None, response=None, actual_code=None,
    #             params=None, headers=None, body=None, logining_errors=None):
    #     request = self.__make_request(endpoint, method, params=params, headers=headers, body=body,
    #                                   logining_errors=logining_errors)
    #     Assertation_model_methods(request).assert_validate_status_code(actual_code=actual_code,
    #                                                                    expected_code=expected_code).asset_validate_jsonschema(
    #         schema=schema, response=response)
    #     return request

    @allure.step("Get request {endpoint} {method}")
    def request(self, endpoint=None, method=None, schema=None, expected_code=None, response=None, actual_code=None,
                params=None, headers=None, body=None, logining_errors=None, metod_validate=None, obj=None,
                parametr=None, model_schema=None):
        request = self.__make_request(endpoint, method, params=params, headers=headers, body=body,
                                      logining_errors=logining_errors)
        request = Assertation_model_methods(request).assert_validate_status_code(actual_code=actual_code,
                                                                                 expected_code=expected_code)
        if metod_validate is not None and metod_validate.lower() == "pydantic":
            return request.validate_pydantic(obj=obj, parametr=parametr, model_schema=model_schema)
        return request.asset_validate_jsonschema(schema=schema, response=response)


class User_Api(BaseModelRequest):

    @allure.step("sign_up {endpoint} {method}")
    def test_post_crate_user(self, body, endpoint="/auth/signup", method="post", schema=None, expected_code=None):
        return self.request(endpoint=endpoint, method=method, body=body, schema=schema, expected_code=expected_code)

    @allure.step("auntificated_user_data {endpoint} {method}")
    def test_get_auntificated_user_data(self, headers, endpoint='/users/current', method="get", schema=None,
                                        expected_code=None):
        return self.request(headers=headers, endpoint=endpoint, method=method, schema=schema,
                            expected_code=expected_code)

    @allure.step("auntificated_user_profile {endpoint} {method}")
    def test_get_auntificated_user_profile(self, headers, endpoint='/users/profile', method="get", schema=None,
                                           expected_code=None):
        return self.request(headers=headers, endpoint=endpoint, method=method, schema=schema,
                            expected_code=expected_code)

    @allure.step("auntificated_user_settings {endpoint} {method}")
    def test_get_auntificated_user_settings(self, headers, endpoint='/users/settings', method="get", schema=None,
                                            expected_code=None):
        return self.request(headers=headers, endpoint=endpoint, method=method, schema=schema,
                            expected_code=expected_code)

    @allure.step("edits_edits_user_settings {endpoint} {method}")
    def test_put_edits_user_profile(self, body, headers=None, endpoint="/users/profile", method="put", schema=None,
                                    expected_code=None,metod_validate=None, obj=None,
                parametr=None, model_schema=None):
        return self.request(endpoint=endpoint, method=method, body=body, schema=schema, expected_code=expected_code,
                            headers=headers,obj=obj, parametr=parametr, model_schema=model_schema,metod_validate=metod_validate)

    @allure.step("edits_user_settings {endpoint} {method}")
    def test_put_edits_user_settings(self, body, headers=None, endpoint="/users/settings", method="put", schema=None,
                                     expected_code=None,metod_validate=None, obj=None,
                parametr=None, model_schema=None):
        return self.request(endpoint=endpoint, method=method, body=body, schema=schema, expected_code=expected_code,
                            headers=headers,obj=obj, parametr=parametr, model_schema=model_schema,metod_validate=metod_validate)

    @allure.step("edits_user_email {endpoint} {method}")
    def test_put_edits_user_email(self, body, headers=None, endpoint="/users/email", method="put", schema=None,
                                  expected_code=None,metod_validate=None, obj=None,
                parametr=None, model_schema=None):
        return self.request(endpoint=endpoint, method=method, body=body, schema=schema, expected_code=expected_code,
                            headers=headers,obj=obj, parametr=parametr, model_schema=model_schema,metod_validate=metod_validate)

    @allure.step("edits_user_password {endpoint} {method}")
    def test_put_edits_user_password(self, body, headers=None, endpoint="/users/password", method="put", schema=None,
                                     expected_code=None,metod_validate=None, obj=None,
                parametr=None, model_schema=None):
        return self.request(endpoint=endpoint, method=method, body=body, schema=schema, expected_code=expected_code,
                            headers=headers,obj=obj, parametr=parametr, model_schema=model_schema,metod_validate=metod_validate)
