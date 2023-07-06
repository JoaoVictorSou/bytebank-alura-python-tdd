from bytebank import Funcionario

def age_test():
    employee = Funcionario("Lucas Oliveira", '01/09/2002', 5000)

    print(f'Teste = {employee.idade}')

age_test()