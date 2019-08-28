import datetime

class Pessoa (object):
    nome = None
    anoNascimento = None
    endereco = None

    def __init__(self, nome, ano, endereco):
        self.nome = nome
        self.anoNascimento = ano
        self.endereco = endereco

    def getIdade (self):
        now = datetime.datetime.now()
        idade = now.year - self.anoNascimento

        print('-------------------------')
        print('Idade de', self.nome, 'é', idade, '\n')
    

    def getNome (self):
        return self.nome

    def getAnoNascimento (self):
        return self.anoNascimento

    def getEndereco (self):
        return self.endereco