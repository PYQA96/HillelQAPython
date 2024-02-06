import pytest

from sources.UTILS import *
from sources.Data_generators.Generators import User_generator

from sources.TEST_MODEL_OBJECT import User_Api, Cars, Expension
from datetime import datetime
from sources.BASE_MODEL_REQUEST import BaseModelRequest, RequestContext

@pytest.fixture(scope="module")
def user():
    payload = User_generator().user_sign_up_data()
    context = RequestContext(
        endpoint='/auth/signup',
        body=payload,
        method="post",
    )
    try:
        r = BaseModelRequest().create_request(context)
        dict_user = {
            "json": r.json(),
            "cookies": {'Cookie': f"sid={r.cookies.get('sid')}"},
            "status_code": r.status_code,
            "payload": payload
        }
        yield dict_user
    except Exception as e:
        raise RuntimeError(f"Failed to create user: {e}")


@pytest.fixture(scope="module")
def created_expensive(user,created_car):
    payload = {
        "carId": created_car.get('id_car'),
        "reportedAt":  f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}",
        "mileage": 15896,
        "liters": 11,
        "totalCost": 11,
        "forceMileage": False
    }
    context = RequestContext(
        endpoint='/expenses',
        body=payload,
        method="post",
        headers=user["cookies"]
    )
    try:
        r = BaseModelRequest().create_request(context)
        dict_car = {
            "json": r.json(),
            "cookies": {'Cookie': f"sid={r.cookies.get('sid')}"},
            "status_code": r.status_code,
            "payload": payload,
            'expensive_id': r.json().get('data', {}).get('id')
        }
        return dict_car
    except Exception as e:
        raise RuntimeError(f"Failed to create user: {e}")


@pytest.fixture(scope="module")
def created_car(user):
    payload = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }
    context = RequestContext(
        endpoint='/cars',
        body=payload,
        method="post",
        headers=user["cookies"]
    )
    try:
        r = BaseModelRequest().create_request(context)
        dict_car = {
            "json": r.json(),
            "cookies": {'Cookie': f"sid={r.cookies.get('sid')}"},
            "status_code": r.status_code,
            "payload": payload,
            'id_car':r.json().get('data', {}).get('id'),
            'id_model':r.json().get('data', {}).get('carModelId'),
            'id_brand': r.json().get('data', {}).get('carBrandId'),
        }
        return dict_car
    except Exception as e:
        raise RuntimeError(f"Failed to create user: {e}")


@pytest.fixture(scope="module")
def set_up_sample():
    return User_Api()


@pytest.fixture(scope="module")
def set_up_car():
    return Cars()


@pytest.fixture(scope="module")
def set_up_expensive():
    return Expension()


@pytest.fixture(scope="module")
def give_user_coockie(user):
    headers = {
        'Cookie': user["cookies"]["Cookie"],
    }
    return headers


@pytest.fixture(scope="module")
def give_user_body(user):
    body_to_request_change_email = {
        "email": f'{random_word}@test.com',
        "password": user["payload"]["password"]
    }
    return body_to_request_change_email
