import inspect
import random
import unittest
from parameterized import parameterized
from project.program import Calculator



class MyTestCase(unittest.TestCase):
    """
    решил покрыть базовые случаии связаные и скалькуятором
    а именно : позитивные + негативные основные , заюзал библиотеку параметризайд
    """

    def setUp(self):
        self.calculator = Calculator

    def tearDown(self):
        del self.calculator

    # параметрические позитивные тесты

    @parameterized.expand([
        (f"{random.randrange(-100, 100)} {random.randrange(-100, 100)}"),
        (f"{random.randrange(0, 100)} {random.randrange(-100, 0)}"),
    ])
    def test_add(self, varaible):
        test_function_name = inspect.currentframe().f_code.co_name
        print(f"Running {test_function_name} with params {varaible}")
        try:
            self.assertIsInstance(self.calculator(varaible).add(), (int,float))
        except Exception as e:
            self.fail(f"Error {str(e)}")

    @parameterized.expand([
        (f"{random.randrange(-100, 100)} {random.randrange(-100, 100)}"),
        (f"{random.randrange(0, 100)} {random.randrange(-100, 0)}"),
    ])
    def test_substrat(self, varaible):
        test_function_name = inspect.currentframe().f_code.co_name
        test_function_name = inspect.currentframe().f_code.co_name
        print(f"Running {test_function_name} with params {varaible}")
        try:
            self.assertIsInstance(self.calculator(varaible).subtract(), (int,float))
        except Exception as e:
            self.fail(f"Error {str(e)}, {self.calculator.subtract(varaible)}")

    @parameterized.expand([
        (f"{random.randrange(-100, 100)} {random.randrange(-100, 100)}"),
        (f"{random.randrange(0, 100)} {random.randrange(-100, 0)}"),
    ])
    def test_multiply(self, varaible):
        test_function_name = inspect.currentframe().f_code.co_name
        print(f"Running {test_function_name} with params {varaible}")
        try:
            self.assertIsInstance(self.calculator(varaible).multiply(), (int,float))
        except Exception as e:
            self.fail(f"Error {str(e)}")

    @parameterized.expand([
        (f"{random.randrange(-100, 100)} {random.randrange(-100, 100)}"),
        (f"{random.randrange(0, 100)} {random.randrange(-100, 0)}"),
    ])
    def test_divide(self, varaible):
        test_function_name = inspect.currentframe().f_code.co_name
        print(f"Running {test_function_name} with params {varaible}")
        try:
            self.assertIsInstance(self.calculator(varaible).divide(), (int, float))
        except Exception as e:
            self.fail(f"Error {str(e)}")

    # негативные параметризованые тесты

    @parameterized.expand([
        ( "add", "test", 2),
        ( "subtract", "test", 2),
        ( "multiply", "test", "test"),
        ( "divide", "test", 0),
        ( "divide", 1, 0),
        ( "add", 2, "test"),
        ( "subtract", 2, "test"),
        ( "multiply", "test", "test"),
        ( "divide", 0, "test"),
        ( "divide", 0, 0),
    ])
    def test_negative_results_tiping(self, func, a, b):
        test_function_name = inspect.currentframe().f_code.co_name
        print(f"Running {test_function_name} with params {a, b}")
        answer = getattr(self.calculator(f"{a}{b}"), func)()
        self.assertIsNone(answer)

if __name__ == '__main__':
    unittest.main()
