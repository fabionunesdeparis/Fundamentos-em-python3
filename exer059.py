from time import sleep
from winsound import Beep
# @Fábio C Nunes - 17.05.20
valor_menu = 0
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
resultado = 0
while valor_menu != 5:
    print('--------- Menu --------- ', end='')
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair ''')
    print('------------------------ ')
    valor_menu = int(input('Escolha uma opção: '))
    #opç 1
    if valor_menu == 1:
        resultado = (valor1 + valor2)
        print('{} + {} = {}'.format(valor1, valor2, resultado))
        sleep(1)
    #opç 2
    elif valor_menu == 2:
        resultado = (valor1 * valor2)
        print('{} x {} = {}'.format(valor1, valor2, resultado))
    #opç3
    elif valor_menu == 3:
        if valor1 > valor2:
            resultado = valor1
            print(' O valor {} é maior que {}'.format(valor1, valor2))
        elif valor2 > valor1:
            resultado = valor2
            print(' O valor {} é maior que {}'.format(valor2, valor1))
        else:
            print('Os valores {} e {} são iguais.'.format(valor1, valor2))
    #opç 4
    elif valor_menu == 4:
        print('Digite os números novamente!!!')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    #opç 5
    elif valor_menu == 5:
        print('Finalizando...')
    #opç menor que 5
    else:
        print('Opção Invalida! Escolha uma opção entre 1 e 5.')
        Beep(2000, 100)
    sleep(1)
print('FIM')
