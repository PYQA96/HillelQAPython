import pytest
from src.conftest import user
from src.Utils import *
from src.base_model import *
from src.pydantics_validators import *


@pytest.mark.usefixtures('user')
class Test_user_created:

    def test_create_user_sucsesfool(self, user):
        print("-" * 50, TYPE_TEST_POSITIVE)
        BaseModelRequest.assert_validate_status_code(user["status_code"], CREATED_STATUS_CODE), ERROR_MESAGES
        BaseModelRequest.asset_validate_jsonschema(user["json"], json_schema_users_created_sucsess), ERROR_MESAGES

    def test_recreate_user(self, user):
        print("-" * 50, TYPE_TEST_NEGATIVE)
        request = BaseModelRequest(f"/auth/signup").make_request("post", body=user["payload"])
        BaseModelRequest.asset_validate_jsonschema(request.json(), json_schema_users_fail)
        BaseModelRequest.assert_validate_status_code(request.status_code, ERROR_STATUS_CODE_CREATED)

    @pytest.mark.parametrize("invalid_json,json_validation_schema,name",
                             [
                                 (
                                         {
                                             "lastName": "Dou",
                                             "email": f"{random_word}@gmail.com",
                                             "password": f'111wWw111',
                                             "repeatPassword": f"111wWw111"
                                         },
                                         json_schema_users_fail,
                                         "without_name"
                                 ), (
                                     {
                                         "name": "John",
                                         "email": f"{random_word}@gmail.com",
                                         "password": f'111wWw111',
                                         "repeatPassword": f"111wWw111"
                                     },
                                     json_schema_users_fail,
                                     "without_lastName"
                             ),
                                 (
                                         {
                                             "name": "John",
                                             "lastName": "Dou",
                                             "password": f'111wWw111',
                                             "repeatPassword": f"111wWw111"
                                         },
                                         json_schema_users_fail,
                                         "without_email"
                                 ),
                                 (
                                         {
                                             "name": "John",
                                             "lastName": "Dou",
                                             "email": f"{random_word}@gmail.com",
                                             "repeatPassword": f"111wWw111"
                                         },
                                         json_schema_users_fail,
                                         "without_password"
                                 ),
                                 (
                                         {
                                             "": "",
                                         },
                                         json_schema_users_fail,
                                         "without_email"
                                 )
                             ]
                             )
    def test_validate_user_field(self, invalid_json, json_validation_schema, name):
        print("-" * 50, TYPE_TEST_NEGATIVE)
        request = BaseModelRequest('/auth/signup').make_request("post", body=invalid_json)
        BaseModelRequest.asset_validate_jsonschema(json.loads(request.text), json_schema_users_fail)
        BaseModelRequest.assert_validate_status_code(request.status_code, ERROR_STATUS_CODE_CREATED)


@pytest.mark.usefixtures("user")
class Test_users_collection_get_information:

    @pytest.mark.parametrize("endpoint,method,code,shema",
                             [
                                 ('/users/current', "get", SUCSESSFUL_STATUS_CODE, json_schema_users_created_sucsess),
                                 ('/users/profile', "get", SUCSESSFUL_STATUS_CODE, json_schema_users_created_auth),
                                 ('/users/settings', "get", SUCSESSFUL_STATUS_CODE, json_schema_users_settings)
                             ]

                             )
    def test_get_methods_users(self, user, endpoint, method, code, shema):
        print("-" * 50, TYPE_TEST_POSITIVE)
        respons = BaseModelRequest(endpoint).make_request(method, headers=user["cookies"])
        BaseModelRequest.assert_validate_status_code(respons.status_code, code)
        BaseModelRequest.asset_validate_jsonschema(respons.json(), shema)

    @pytest.mark.parametrize("endpoint,method,code,shema,head",
                             [
                                 ('/users/current', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, headers_fake),
                                 ('/users/current', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, ""),
                                 ('/users/current', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, None),
                                 ('/users/profile', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  headers_fake),
                                 ('/users/profile', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, ""),
                                 ('/users/profile', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, None),
                                 ('/users/settings', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  headers_fake),
                                 ('/users/settings', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, ""),
                                 ('/users/settings', "get", EROR_STATUS_CODE_AUTH, json_schema_users_fail, None),

                             ]
                             )
    def test_negative_get_methods_users(self, endpoint, method, code, shema, head):
        print("-" * 50, TYPE_TEST_NEGATIVE)
        respons = BaseModelRequest(endpoint).make_request(method, headers=head)
        BaseModelRequest.assert_validate_status_code(respons.status_code, code)
        BaseModelRequest.asset_validate_jsonschema(respons.json(), shema)


@pytest.mark.usefixtures("user")
class Test_users_collection_edit_profile:

    def test_edits_users_profile(self, user):
        print("-" * 50, TYPE_TEST_POSITIVE)
        headers = {
            'Cookie': user["cookies"]["Cookie"],
        }
        request = BaseModelRequest('/users/profile').make_request("put", body=body_to_request_profile_edit,
                                                                  headers=headers)
        BaseModelRequest.asset_validate_jsonschema(request.json(), json_schema_users_updated)
        BaseModelRequest.assert_validate_status_code(request.status_code, SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("parametetr,obj",
                             [
                                 ({
                                      "photo": "Notest.jpg",
                                      "name": "Test",
                                      "lastName": "Notest",
                                      "dateBirth": "2021-03-17T15:21:05.000Z",
                                      "country": "Notest"
                                  }, "name"), ({
                                                   "photo": "Notest.jpg",
                                                   "name": "Notest",
                                                   "lastName": "Test",
                                                   "dateBirth": "2021-03-17T15:21:05.000Z",
                                                   "country": "Notest"
                                               }, "lastName"),
                                 ({
                                      "photo": "Notest.jpg",
                                      "name": "Notest",
                                      "lastName": "Notest",
                                      "dateBirth": "2021-03-17T15:21:05.000Z",
                                      "country": "Test"
                                  }, "country")
                             ]
                             )
    def test_edits_users_profile_parameters(self, user, parametetr, obj):
        print("-" * 50, TYPE_TEST_NEGATIVE)
        headers = {
            'Cookie': user["cookies"]["Cookie"],
        }
        print(user["cookies"]["Cookie"])
        response = BaseModelRequest('/users/profile').make_request("put", body=parametetr, headers=headers)
        BaseModelRequest.validate_pydantic(response.json(), obj, ApiResponse)
        BaseModelRequest.assert_validate_status_code(response.status_code, SUCSESSFUL_STATUS_CODE)

    def test_edits_users_ettings(self, user):
        print("-" * 50, TYPE_TEST_POSITIVE)
        headers = {
            'Cookie': user["cookies"]["Cookie"],
        }
        request = BaseModelRequest('/users/settings').make_request("put", body=body_to_request_users_settings,
                                                                   headers=headers)
        BaseModelRequest.asset_validate_jsonschema(request.json(), json_schema_profile_updated)
        BaseModelRequest.assert_validate_status_code(request.status_code, SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("parametetr,obj_in_json,parametr_to_change",
                             [
                                 ({
                                      "currency": "uah",
                                      "distanceUnits": "km"
                                  }, "currency", "uah"),
                                 ({
                                      "currency": "usd",
                                      "distanceUnits": "ml"
                                  }, "distanceUnits", "ml"),

                             ]
                             )
    def test_edits_users_settings(self, user, parametetr, obj_in_json, parametr_to_change):
        print("-" * 50, TYPE_TEST_NEGATIVE)
        headers = {
            'Cookie': user["cookies"]["Cookie"],
        }
        response = BaseModelRequest('/users/settings').make_request("put", body=parametetr, headers=headers)

        BaseModelRequest.validate_pydantic(response.json(), obj_in_json, ApiResponse_setings, parametr_to_change)
        BaseModelRequest.assert_validate_status_code(response.status_code, SUCSESSFUL_STATUS_CODE)


    def test_change_user_email(self, user):
        print("-" * 50, TYPE_TEST_POSITIVE)
        headers = {
            'Cookie': user["cookies"]["Cookie"],
        }
        body_to_request_change_email = {
            "email": f'{random_word}@test.com',
            "password": user["payload"]["password"]
        }

        request = BaseModelRequest('/users/email').make_request("put", body=body_to_request_change_email,
                                                                   headers=headers)
        BaseModelRequest.asset_validate_jsonschema(request.json(), json_schema_email_ok)
        BaseModelRequest.assert_validate_status_code(request.status_code, SUCSESSFUL_STATUS_CODE)


