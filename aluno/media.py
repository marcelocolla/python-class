def calcularMedia (p1, p2, p3):
    return (p1 + p2 + p3) / 3

def alunoAprovado (media):
    if media >= 6:
        print('Aprovado')
    else:
        print('reprovado')

alunoAprovado(calcularMedia(8, 5, 5))