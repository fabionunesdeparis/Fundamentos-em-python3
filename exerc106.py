# @Fábio C Nunes - 28.06.20
def ajuda(valor):
    print('\033[34;43m-' * 35)
    print(f'Acessando Manual do comando {valor}')
    print('-' * 35)
    print('\033[m')
    print('\033[32;44m')
    help(valor)
    print('\033[m', end='')

def tela():
    print('\033[1;31;47m-' * 35)
    print('{:^35}'.format('Sistema de ajuda - Pyhelp'))
    print('-' * 35,)
    print('\033[m', end = '')


#Main
resp = ''
while True:
    tela()
    var = str(input('Qual comando deseja consultar? '))
    resp = var.upper().strip()
    if resp == 'FIM':
        break
    else:
        ajuda(var)
