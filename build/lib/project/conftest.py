import pytest
from project.program import Calculator


@pytest.fixture()
def calc_set_up_nums():
    return Calculator
