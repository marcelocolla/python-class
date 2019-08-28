class Aluno:
    nome = None
    ra = None
    periodo = None

    def __init__ (self, nome, ra, periodo):
        self.setAluno(nome)
        self.setRa(ra)
        self.setPeriodo(periodo)

    def setAluno (self, nome):
        self.nome = nome

    def getAluno (self):
        print('Informações do Aluno:')
        print('Nome: ', self.nome)
        print('R.A: ', self.getRa())
        print('Período: ', self.getPeriodo(), '\n')

    def setRa (self, ra):
        self.ra = ra

    def getRa (self):
        return self.ra

    def setPeriodo (self, periodo):
        self.periodo = periodo

    def getPeriodo (self):
        return self.periodo

    def calcularMedia (self, p1, p2):
        media = (p1 + p2) / 2

        if media > 6:
            self.setPeriodo(int(self.periodo) + 1)
