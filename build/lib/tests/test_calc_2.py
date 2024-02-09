import pytest
from contextlib import nullcontext as dus_not_raise
from project.conftest import calc_set_up_nums


@pytest.mark.usefixtures("calc_set_up_nums")
class Test_calc:

    def invoke_method(self, calculator, method_name):
        methods_mapping = {
            "add": calculator.add(),
            "divide": calculator.divide(),
            "multiply": calculator.multiply(),
            "subtract": calculator.subtract(),

        }
        return methods_mapping[method_name]

    @pytest.mark.parametrize("x,result,error,methods",
                             [
                                 ("1 2", 3, dus_not_raise(), "add"),
                                 ("2 2", 4, dus_not_raise(), "add"),
                                 ("2 2", 0, dus_not_raise(), "subtract"),
                                 ("-2 -2", 0, dus_not_raise(), "subtract"),
                                 ("2 2", 4, dus_not_raise(), "multiply"),
                                 ("2 0", 0, dus_not_raise(), "multiply"),
                                 ("2 2", 1, dus_not_raise(), "divide"),

                             ])
    def test_positive_allmetods(self, calc_set_up_nums, x, result, error, methods):
        with error:
            print(id(calc_set_up_nums(x)))
            assert self.invoke_method(calc_set_up_nums(x), methods) == result

    @pytest.mark.parametrize("x,result,error,methods",
                             [
                                 ("  ", None, dus_not_raise(), "add"),
                                 ("a", None, dus_not_raise(), "add"),
                                 ("  ", None, dus_not_raise(), "subtract"),
                                 ("a", None, dus_not_raise(), "subtract"),
                                 ("  ", None, dus_not_raise(), "multiply"),
                                 ("1", None, dus_not_raise(), "multiply"),
                                 ("  ", None, dus_not_raise(), "divide"),

                             ])
    def test_negative_allmetods(self, calc_set_up_nums, x, result, error, methods):

        with error:
            print(id(calc_set_up_nums(x)))
            assert self.invoke_method(calc_set_up_nums(x), methods) == result

    def test_naming_methods(self, calc_set_up_nums):
        methods_in_fixture = sorted(
            [i for i in dir(calc_set_up_nums) if not str(i).startswith("__") and not str(i).startswith("val")])
        metods = ['add', 'divide', 'multiply', 'subtract']
        for metod_check, metod in zip(metods, methods_in_fixture):
            assert metod == metod_check
