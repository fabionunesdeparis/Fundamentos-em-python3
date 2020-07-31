from random import randint
from time import sleep
# @Fábio C Nunes - 08.06.20 Ex 88
#tela
print('--' * 20)
print('{:^40}'.format('Palpiteiro'))
print('--' * 20)
#numero de apostas e numeros randomicos
número_jogos = int(input('Número de joos que deseja fazer:  '))
print('--' * 20)
jogos = []
totaljogos = []
n = 0
cont = 0
for i in range(0, número_jogos):
    while cont < 6:
        n = randint(1,61)
        if n not in jogos:
            jogos.append(n)
            cont += 1
    jogos.sort()
    totaljogos.append(jogos[:])
    jogos.clear()
    cont = 0

#Mostrando jogos na tela
for i in range(0,len(totaljogos)):
    print(f'Jogo {i+1:^3}: ', end='')
    for j in range(0,6):
        print(f'{totaljogos[i][j]:^5}', end='')
    print()
    sleep(1)
print('--' * 20)
print(' {:^40}'.format('Boa Sorte !'))
print('--' * 20)
