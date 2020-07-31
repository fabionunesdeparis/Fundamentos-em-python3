# @Fábio C Nunes - 22.06.20
from time import sleep

def contador(a, b, c):
    #Cabeçalho
    print('-' * 35)
    print(f'Contador de {a} até {b} - de {c} em {c}.')
    sleep(1)
    print('-' * 35)
    for i in range(a, b, c):
        print(i, end=' ')
        sleep(0.5)
    print(' Fim ')
    print('-' * 35)


#Main.
#Contagem de 1 até 10.
contador(1, 11, 1)
contador(10, 0, -2)
#Contagem personalizada
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if fim < inicio and passo > 0:
    passo = passo - (passo * 2)
if passo == 0 :
    passo = 1
contador(inicio, fim, passo)
