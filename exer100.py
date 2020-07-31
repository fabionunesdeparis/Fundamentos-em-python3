# @Fábio C Nunes - 23.06.20
from random import randint
from time import sleep

def sorteia():
    print('Sorteando valores')

    for i in range(0, 5):
        números.append(randint(1, 10))
        print(números[i], end=' ')
        sleep(0.5)


def somapar():
    totpar = 0

    for i in range(0, 5):
        if números[i] % 2 == 0:
            totpar += números[i]
    print()
    print(f'A somatória da lista {números} é igual a: {totpar}.')

#Main
números = []
sorteia()
somapar()