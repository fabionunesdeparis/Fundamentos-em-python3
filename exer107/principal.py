# @Fábio C Nunes - 30.06.20
from exer107 import moeda
while True:
    valor = str(input('Digite o preço: R$'))
    if valor.isnumeric():
        valor = float(valor)
        moeda.metade(valor)
        moeda.dobro(valor)
        moeda.aumentar(valor)
        moeda.diminuir(valor)
        break
    else:
        print('Digite um valor numérico! ')