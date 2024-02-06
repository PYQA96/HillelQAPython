import pytest
from src.ASERTATION_MODEL import Assertation_model_methods
from src.Data_generators.Generators import User_generator
from src.UTILS import *
from src.PYDANTICS_VALIDATORS import *



@pytest.mark.usefixtures('set_up_sample')
@pytest.mark.usefixtures('user')
class Test_user_created:
    @pytest.mark.Smok
    def test_create_user_sucsesfool(self, user):
        Assertation_model_methods(user["json"]).assert_validate_status_code(
            CREATED_STATUS_CODE,user["status_code"]).asset_validate_jsonschema(json_schema_users_created_sucsess,
                                                                                user["json"])

    def test_recreate_user(self, user, set_up_sample):
        set_up_sample.test_post_crate_user(body=user["payload"], schema=json_schema_users_fail,
                                           expected_code=ERROR_STATUS_CODE_CREATED)

    @pytest.mark.parametrize("invalid_json,json_validation_schema,name",
                             [
                                 (
                                         User_generator().last_Name().email().password().repeat_Password().cusstom_bild(),
                                         json_schema_users_fail,
                                         "without_name"
                                 ), (
                                         User_generator().name().email().password().repeat_Password().cusstom_bild(),
                                         json_schema_users_fail,
                                         "without_lastName"
                             ),
                                 (
                                         User_generator().name().last_Name().password().repeat_Password().cusstom_bild(),
                                         json_schema_users_fail,
                                         "without_email"
                                 ),
                                 (
                                         User_generator().name().last_Name().repeat_Password().cusstom_bild(),
                                         json_schema_users_fail,
                                         "without_password"
                                 ),
                                 (
                                         {
                                             None: None,
                                         },
                                         json_schema_users_fail,
                                         "without_email"
                                 )
                             ]
                             )
    def test_validate_user_field(self, invalid_json, json_validation_schema, name, set_up_sample):
        print(invalid_json)
        set_up_sample.test_post_crate_user(body=invalid_json, schema=json_validation_schema,
                                           expected_code=ERROR_STATUS_CODE_CREATED)


@pytest.mark.usefixtures('set_up_sample')
@pytest.mark.usefixtures("user")
class Test_users_collection_get_information:

    @pytest.mark.parametrize("endpoint,code,shema",
                             [
                                 ('test_get_auntificated_user_data', SUCSESSFUL_STATUS_CODE,
                                  json_schema_users_created_sucsess),
                                 ('test_get_auntificated_user_profile', SUCSESSFUL_STATUS_CODE,
                                  json_schema_users_created_auth),
                                 ('test_get_auntificated_user_settings', SUCSESSFUL_STATUS_CODE,
                                  json_schema_users_settings)
                             ]

                             )
    def test_get_methods_users(self, user, endpoint, code, shema, set_up_sample):
        getattr(set_up_sample, endpoint)(headers=user["cookies"], expected_code=code, schema=shema)

    @pytest.mark.parametrize("endpoint,code,shema,head",
                             [
                                 ('test_get_auntificated_user_data', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  headers_fake),
                                 ('test_get_auntificated_user_profile', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  ""),
                                 ('test_get_auntificated_user_settings', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  None),
                                 ('test_get_auntificated_user_data', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  headers_fake),
                                 ('test_get_auntificated_user_profile', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  ""),
                                 ('test_get_auntificated_user_settings', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  None),
                                 ('test_get_auntificated_user_data', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  headers_fake),
                                 ('test_get_auntificated_user_profile', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  ""),
                                 ('test_get_auntificated_user_settings', EROR_STATUS_CODE_AUTH, json_schema_users_fail,
                                  None),

                             ]
                             )
    def test_negative_get_methods_users(self, endpoint, code, shema, head, set_up_sample):
        getattr(set_up_sample, endpoint)(headers=head, expected_code=code, schema=shema)


@pytest.mark.usefixtures("give_user_coockie")
@pytest.mark.usefixtures('set_up_sample')
@pytest.mark.usefixtures("user")
class Test_users_collection_edit_profile:

    def test_edits_users_profile(self, set_up_sample, give_user_coockie):
        set_up_sample.test_put_edits_user_profile(body=body_to_request_profile_edit, headers=give_user_coockie,
                                                  schema=json_schema_users_updated,
                                                  expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("parametetr,key",
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
    def test_edits_users_profile_parameters(self, parametetr,  give_user_coockie, set_up_sample,key):
        set_up_sample.test_put_edits_user_profile(body=parametetr, headers=give_user_coockie, metod_validate=True,
                                                  model_schema=ApiResponse,
                                                  expected_code=SUCSESSFUL_STATUS_CODE)

    def test_edits_users_ettings(self, give_user_coockie, set_up_sample):
        set_up_sample.test_put_edits_user_settings(body=body_to_request_users_settings, headers=give_user_coockie,
                                                   schema=json_schema_profile_updated,
                                                   expected_code=SUCSESSFUL_STATUS_CODE)

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
                                 ({
                                      "currency": "uah",
                                      "distanceUnits": "km"
                                  }, ["currency", "distanceUnits"], ["uah", "km"]),

                             ]
                             )
    def test_edits_users_settings(self, user, parametetr, obj_in_json, parametr_to_change, give_user_coockie,
                                  set_up_sample):
        set_up_sample.test_put_edits_user_settings(body=parametetr, headers=give_user_coockie,
                                                   metod_validate=False,
                                                   key=obj_in_json, value=parametr_to_change,massivkey="data",
                                                   model_schema=ApiResponse_setings,
                                                   expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.usefixtures('give_user_body')
    def test_change_user_email(self, give_user_body, set_up_sample, give_user_coockie):
        set_up_sample.test_put_edits_user_email(body=give_user_body, headers=give_user_coockie,
                                                expected_code=SUCSESSFUL_STATUS_CODE, schema=json_schema_email_ok)
