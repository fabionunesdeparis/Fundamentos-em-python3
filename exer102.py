# @Fábio C. Nunes - 24.06.20
def fatorial(fat, mostrar = False):
    """
    Calcula o fatorial de um número
    :param fat: É o valor a ser calsulado o fatorial do número
    :param mostrar: Podendo ter o argumento True ou False, para mostrar impresso na tela ou não as etapas do cálculo.
    :return: não retorna nenhum paramêtro
    """
    from math import factorial
    if mostrar == False:
        print(f'{fat}! =', factorial(fat))
    else:
        cont = total = fat
        print(f'{fat}! = ', end='')
        while cont > 1:
            total = total * (cont -1)
            print(cont, end=' x ')
            cont -= 1
        print(f'1 = {total}')


#Main
opc = ' '
n = int(input('Digite um valor inteiro: '))
while opc not in 'SN':
    opc = str(input('Deseja Visualizar o calculo? [S/N]: ')).strip().upper()[0]
if 'S' in opc:
    segpar = True
else:
    segpar = False
fatorial(n, segpar)