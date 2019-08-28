#Exercicio2
def converteTemperatura (graus):
    f = (9 * graus + 160) / 5
    k = (graus + 273)

    print('Celsius:', graus)
    print('Fahrenheit:', f)
    print('Kelvin:', k)

converteTemperatura(25)