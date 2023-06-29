from datetime import datetime, date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        print(self._data_nascimento)
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @property
    def idade(self):
        ano_atual = datetime.now()
        
        delta_idade = ano_atual.year - self._data_nascimento.year
        
        mes_adiante = ano_atual.month > self._data_nascimento.month
        mes_adiante_ou_igual = ano_atual.month >= self._data_nascimento.month
        dia_adiante_ou_igual = ano_atual.day >= self._data_nascimento.day

        idade_atual = delta_idade if mes_adiante or (mes_adiante_ou_igual and dia_adiante_ou_igual) else (delta_idade - 1)
        
        return idade_atual
    
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'