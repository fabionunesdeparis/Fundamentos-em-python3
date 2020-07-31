# @Fábio C Nunes - 16.06.20
from random import randint
from time import sleep
from operator import itemgetter
#Variavéis
d = ''
njog = str()
dado = {}
ranking = {}
#sorteando e Adicionando ao dicionario os valores
for i in range(1, 5):
    d = randint(1, 6)
    njog = 'Jogador ' + str(i)
    dado[njog] = d
#Apresentando resultado dos dados
print('-' * 20)
print('Sorteando dados...')
print('-' * 20)
for i, j in dado.items():
    print(f'{i} tirou : {j}')
    sleep(1)
print('-' * 20)

#Apresentando jogadores vencedores em ordem decrescente
print('-' * 20)
print('Apresentando Vencedores')
print('-' * 20)
ranking = sorted(dado.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(1)