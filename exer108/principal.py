# @Fábio C Nunes - 30.06.20
from exer108 import moeda
while True:
    valor = str(input('Digite o preço: R$ '))
    print('-' * 50)
    if valor.isnumeric():
        valor = float(valor)
        print(f'A metade de {moeda.moeda(valor)} é: \n{moeda.metade(valor, True)}')
        print('-' * 50)
        print(f'O dobro de {moeda.moeda(valor)} é: \n{moeda.dobro(valor, True)}')
        print('-' * 50)
        print(f'O valor {moeda.moeda(valor)} acrecido de 10% é de:  \n{moeda.aumentar(valor, True)}')
        print('-' * 50)
        print(f'O valor {moeda.moeda(valor)} decrecido de 10% é de: \n{moeda.diminuir(valor, True)}')
        print('-' * 50)
        break
    else:
        print('Digite um valor numérico! ')
