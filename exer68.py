from random import randint # @Fábio C Nunes 19.05.20
print('-' * 20)
print('{:^20}'.format('Par ou ímpar'))
print('-' * 20)
cont = 0
while True:
    perg = ' '
    num_pc = randint(1,10)
    num_usu = int(input('Escolha um número: '))
    while perg not in 'PpIi':
        perg = str(input('Par ou ímpar? [P/I]: ')).lower().strip()[0]
        print('-' * 20)
    print(f'O Computador escolheu: {num_pc}')
    print(f'Você escolheu: {num_usu}')
    print(f'O Total foi: {num_pc+num_usu}')
    #verificando quem ganhou
    #ganhou par
    if (perg == 'p') and ((num_pc + num_usu) % 2) == 0:
        cont += 1
        print('Você Venceu! Deu Par')
        print('-' * 20)
    #ganhou Impar
    elif (perg == 'i') and ((num_pc + num_usu) % 2) != 0:
        cont += 1
        print('Você Venceu! Deu Ímpar')
        print('-' * 20)
    else:
        print('Você perdeu!')
        print('-' * 20)
        break
print(f'Nº de vitórias acumuladas: {cont}')