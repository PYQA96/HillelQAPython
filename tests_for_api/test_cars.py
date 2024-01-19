import pytest
from src.ASERTATION_MODEL import Assertation_model_methods
from src.UTILS import *
from src.PYDANTICS_VALIDATORS import *
from src.STATIC_METHODS import StatisMethod


@pytest.mark.usefixtures('set_up_car')
@pytest.mark.usefixtures('user')
@pytest.mark.usefixtures('created_car')
class Test_cars:

    def test_create(self, created_car):
        Assertation_model_methods(created_car.get("json")).assert_validate_status_code(created_car.get("status_code"),
                                                                                       CREATED_STATUS_CODE).asset_validate_jsonschema(
            schema=created_car_sucsessfull, response=created_car.get("json"))

    @pytest.mark.parametrize(f"body,massiv_key,obj_in_massiv",
                             [
                                 (
                                         {
                                             "carModelId": 1,
                                             "mileage": 1000
                                         }, "message", "Car brand id is required"
                                 ),
                                 (
                                         {
                                             "carBrandId": 1,
                                             "mileage": 1000
                                         }, "message", "Car model id is required"
                                 ),
                                 (
                                         {
                                             "carBrandId": 1,
                                             "carModelId": 1,
                                         }, "message", "incorect"
                                 )
                             ]
                             )
    def test_created_user_with_incorected_params(self, set_up_car, created_car, body, obj_in_massiv, massiv_key, user):
        set_up_car.test_post_create_a_new_car(headers=user.get("cookies"), body=body, metod_validate=False,
                                              model_schema=ApiResponseCar, obj=obj_in_massiv, massivkey=massiv_key)

    def test_gets_car_barnd(self, set_up_car, created_car):
        set_up_car.test_get_car_brend(headers=created_car.get("cookies"), expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("headers,status_code", [
        (headers_fake, SUCSESSFUL_STATUS_CODE),
        (None, SUCSESSFUL_STATUS_CODE)

    ])
    def test_gets_car_barnd_negative(self, set_up_car, created_car, headers, status_code):
        set_up_car.test_get_car_brend(headers=headers, expected_code=status_code)

    def test_get_car_brands_by_id(self, set_up_car, created_car):
        set_up_car.test_get_car_brend_by_id(ids='1', headers=created_car.get("cookies"),
                                            expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("headers,status_code,id", [
        (headers_fake, SUCSESSFUL_STATUS_CODE, 1),
        (None, SUCSESSFUL_STATUS_CODE, "")

    ])
    def test_get_car_brands_by_id_negative(self, set_up_car, created_car, headers, status_code, id):
        set_up_car.test_get_car_brend_by_id(ids=id, headers=headers, expected_code=SUCSESSFUL_STATUS_CODE)

    def test_get_car_model_by_id(self, set_up_car, created_car):
        set_up_car.test_get_car_model_by_id(ids='1', headers=created_car.get("cookies"),
                                            expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.parametrize("headers,status_code,id", [
        (headers_fake, SUCSESSFUL_STATUS_CODE, 1),
        (None, SUCSESSFUL_STATUS_CODE, "")

    ])
    def test_get_car_model_by_id_negative(self, set_up_car, created_car, headers, status_code, id):
        set_up_car.test_get_car_model_by_id(ids=id, headers=headers, expected_code=SUCSESSFUL_STATUS_CODE)
