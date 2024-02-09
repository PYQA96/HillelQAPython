import pytest
from sources.asertation_midek import Assertation_model_methods
from sources.utils import *
from sources.pydantic_validator import *
from sources.static_method import StatisMethod
from contextlib import nullcontext as dus_not_raise
from datetime import datetime


@pytest.mark.usefixtures('set_up_expensive')
@pytest.mark.usefixtures('user')
@pytest.mark.usefixtures('created_expensive')
class Test_Expensiv:

    def test_create_an_expensiv(self, set_up_expensive, created_expensive):
        Assertation_model_methods(created_expensive.get("json")).assert_validate_status_code(
            actual_code=created_expensive.get("status_code"),
            expected_code=SUCSESSFUL_STATUS_CODE).asset_validate_jsonschema(schema=sucsessful_masage_expenses_created,
                                                                            response=created_expensive.get("json"))

    @pytest.mark.parametrize(f"boby,obj,parametr,erorr,code,", [
        (
                {
                    "reportedAt": "2024-1-19",
                    "mileage": 15896,
                    "liters": 11,
                    "totalCost": 11,
                    "forceMileage": False
                }, "message", "Car id is required", dus_not_raise(), ERROR_STATUS_CODE_CREATED
        ),
        (
                {
                    "carId": 93519,
                    "mileage": 15896,
                    "liters": 11,
                    "totalCost": 11,
                    "forceMileage": False
                }, "message", "Report date is required", dus_not_raise(), ERROR_STATUS_CODE_CREATED
        ),
        (
                {
                    "carId": 93519,
                    "reportedAt": "2024-1-19",
                    "liters": 11,
                    "totalCost": 11,
                    "forceMileage": False
                }, "message", "Mileage is required", dus_not_raise(), ERROR_STATUS_CODE_CREATED
        ),
        (
                {
                    "carId": 93519,
                    "reportedAt": "2024-1-19",
                    "mileage": 15896,
                    "totalCost": 11,
                    "forceMileage": False
                }, "message", "Liters field is required", dus_not_raise(), ERROR_STATUS_CODE_CREATED
        ),

    ])
    def test_negative_expensives_create_with_oncorect_params(self, boby, obj, parametr, set_up_expensive, code, erorr,
                                                             user):
        with erorr:
            set_up_expensive.test_post_create_a_expenses(body=boby, headers=user.get("cookies"), metod_validate=False,
                                                         model_schema=ApiResponseCar)

    def test_get_all_expenses(self, user, set_up_expensive):
        set_up_expensive.test_get_all_expenses(headers=user.get("cookies"), expected_code=SUCSESSFUL_STATUS_CODE,
                                               schema=all_expenses)

    def test_get_expenses_by_id(self, user, set_up_expensive, created_expensive):
        print(created_expensive.get('expensive_id'))
        set_up_expensive.test_get_expenses_an_id(headers=user.get("cookies"), ids=created_expensive.get('expensive_id'),
                                                 expected_code=SUCSESSFUL_STATUS_CODE)

    @pytest.mark.usefixtures('created_car')
    def test_put_expensive(self, user, set_up_expensive, created_expensive, created_car):
        payload = {
            "carId": created_car.get('id_car'),
            "reportedAt": f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}",
            "mileage": 15896,
            "liters": 11,
            "totalCost": 11,
            "forceMileage": False
        }
        set_up_expensive.test_put_edit_expenses_an_id(body=payload, headers=user.get("cookies"),
                                                      ids=created_expensive.get('expensive_id'),
                                                      expected_code=SUCSESSFUL_STATUS_CODE)
