import pytest
from src.BASE_MODEL_REQUEST import BaseModelRequest, User_Api
from src.BASE_MODEL_REQUEST import BaseModelRequest
from src.UTILS import *


@pytest.fixture(scope="module")
def user():
    letters = string.ascii_lowercase
    payload = {
        "name": "John",
        "lastName": "Dou",
        "email": f"{''.join(random.choice(letters) for _ in range(6))}@gmail.com",
        "password": f"111wWw111",
        "repeatPassword": f"111wWw111"
    }
    try:
        r = BaseModelRequest().request('/auth/signup',"post", body=payload)
        dict_user = {
            "json" : r.json(),
            "cookies" :  {'Cookie':f"sid={r.cookies.get('sid')}"},
            "status_code" : r.status_code,
            "payload" : payload
        }
        return dict_user
    except Exception as e:
        raise RuntimeError(f"Failed to create user: {e}")


@pytest.fixture(scope="module")
def set_up_sample():
    return User_Api()



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