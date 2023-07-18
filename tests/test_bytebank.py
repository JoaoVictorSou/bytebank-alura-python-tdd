from datetime import datetime
from src.bytebank import Funcionario

class TestClass:
    def test_age_to_2000_03_13_date_should_return_correct_years_old(self):
        # Given
        entry = '13/03/2000'
        current_date = datetime.now()
        expect = 23
        
        if current_date.month < 3:
            expect -= 1
        elif current_date.day < 13:
            expect -= 1

        # When
        employee = Funcionario('João', entry, 2000)
        result = employee.idade

        # Then
        assert result == expect