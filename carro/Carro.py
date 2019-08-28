class Carro (object):
    cor = None
    marca = None
    modelo = None
    ano = None

    def __init__(self, marca, cor, ano, modelo):
        self.setMarca(marca)
        self.setCor(cor)
        self.setAno(ano)
        self.setModelo(modelo)


    def getCarro (self):
        print('Informações do Carro:')
        print('Marca:', self.getMarca())
        print('Cor:', self.getCor())
        print('Modelo:', self.getModelo())
        print('Ano:', self.getAno(), '\n')

    def getCor (self):
        return self.cor

    def setCor (self, cor):
        self.cor = cor

    def getMarca (self):
        return self.marca

    def setMarca (self, marca):
        self.marca = marca

    def getModelo (self):
        return self.modelo

    def setModelo (self, modelo):
        self.modelo = modelo

    def getAno (self):
        return self.ano

    def setAno (self, ano):
        self.ano = ano
    