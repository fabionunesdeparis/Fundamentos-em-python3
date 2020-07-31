# @Fábio C Nunes - 22.06.20
from time import sleep
def maior(val):
    maior_num = max(val)
    print('-' * len(val * 4))
    print('Analisando os valores digitados...')
    print('-' * len(val * 4))
    for i in range (0, len(val)):
        print(val[i], end=' ')
        sleep(0.5)
    print()
    print('-' * len(val * 4))
    print(f'Foram digitados {len(val)} números.')
    print(f'O maior valor digitado foi: {maior_num}')


#Main
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if 'N' in c:
        break
maior(valores)