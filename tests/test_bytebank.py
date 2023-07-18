from datetime import datetime
from src.bytebank import Funcionario

class TestClass:
    def test_age_to_2000_03_13_date_should_return_23(self):
        # Given
        entry = '13/03/2000'
        expect = 23

        # When
        employee = Funcionario('João', entry, 2000)
        result = employee.idade

        # Then
        assert result == expect