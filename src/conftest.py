import json
import pytest
from project.program import Calculator
from src.base_model import BaseModelRequest
import random
import string

@pytest.fixture(scope="class")
def user():
    letters = string.ascii_lowercase
    payload = {
        "name": "John",
        "lastName": "Dou",
        "email": f"{''.join(random.choice(letters) for _ in range(6))}@gmail.com",
        "password": f"111wWw111",
        "repeatPassword": f"111wWw111"
    }
    r = BaseModelRequest('/auth/signup').make_request("post", body=payload)
    dict_user = {
        "json" : r.json(),
        "cookies" :  {'Cookie':f"sid={r.cookies.get('sid')}"},
        "status_code" : r.status_code,
        "payload" : payload
    }
    return dict_user