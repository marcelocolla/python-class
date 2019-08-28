from Pessoa import *

class Funcionario(Pessoa):
    salario = None
    cargo = None

    def __init__(self, nome, ano, endereco, salario):
        super().__init__(nome, ano, endereco)
        self.setSalario(salario)

    def getFuncionario(self):
        print('Informações do funcionário:')
        print('Nome:', self.getNome())
        print('Data de Nascimento:', self.getAnoNascimento())
        print('Endereço:', self.getEndereco())
        print('Salario: R$', self.getSalario(), '\n')

    def getSalario (self):
        return self.salario
    
    def setSalario (self, salario):
        self.salario = salario