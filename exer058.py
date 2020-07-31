import random # @Fábio C Nunes 16.05.20
cont = 0
numero_usu = 0
print('Sou o computador e vou pensar em um número entre 0 e 10!')
numero_usu = int(input('Adivinhe que número é: '))
while numero_usu > 10:
    print('O número deve ser menor que 10. Tente novamente.')
    numero_usu = int(input('Adivinhe que número é: '))

numero_pc = random.randint(0, 10)
print('-' * 20)
while numero_usu != numero_pc:
    if numero_usu < numero_pc:
        cont += 1
        print('Você errou! Um pouco mais!!!')
        numero_usu = int(input('Tente novamente: '))
        print('-' * 20)
    elif numero_usu > numero_pc and numero_usu:
        cont += 1
        print('Você errou! Um pouco menos!!!')
        numero_usu = int(input('Tente novamente: '))
        print('-' * 20)
if numero_usu == numero_pc:
    print('Voce acertou!! Parabéns!!!')
    print('Nª de tentativas: {}'.format(cont))
    print('-' * 20)
