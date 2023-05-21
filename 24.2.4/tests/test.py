import pytest
from app.calculator import Calculator

class TestsCalc:
    def setup(self):
        self.calculator = Calculator

    def test_multyply_success(self):
        assert self.calculator.multiply(self, 2, 2) == 4, 'Ошибка в умножении'

    def test_adding_success(self):
        assert self.calculator.adding(self, 1, 1) == 2, 'Ошибка в сложении'

    def test_division_success(self):
        assert self.calculator.division(self, 4, 2) == 2, 'Ошибка в делении'

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 4, 2) == 2, 'Ошибка в вычитании'

    def test_adding_unsuccess(self):
        assert self.calculator.adding(self, 1, 1) == 3, 'Ошибка негативного теста на сложение'

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calculator.division(self, 4, 0), 'Ошибка при делении на ноль'

    def teardown(self):
        print('Выполенение метода Teardown')