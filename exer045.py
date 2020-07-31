import random,time,winsound
# @ Fábio C Nunes 13/05/20 - Software Jokenpo
resp_jogo = random.randint(1,3)
#sorteando resposta do jogo
if resp_jogo == 1:
    jogo_pc = ('Pedra')
elif resp_jogo == 2:
    jogo_pc = ('Papel')
elif resp_jogo == 3:
    jogo_pc = ('Tesoura')
# recebendo escolha do usuário
print('Vamos Jogar!!! ')
print('''
[1] - Pedra
[2] - Papel
[3] - Tesoura
''')
resp_usu = int(input(' Escolha uma opção: '))
if resp_usu == 1:
    jogo_usu = ('Pedra')
elif resp_usu == 2:
    jogo_usu = ('Papel')
elif resp_usu == 3:
    jogo_usu = ('Tesoura')
else:
    print('Escolha a opção 1, 2 ou 3.')

# animação
print('\033[31mJo\033[m')
winsound.Beep(2500,60)
time.sleep(1)
print('\033[34m   Ken\033[m')
winsound.Beep(2500,100)
time.sleep(1)
print('\033[33mPo\033[m')
winsound.Beep(2500,60)
time.sleep(1)
#resultado na tela
print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
print('Computador escolheu: \n{:^33} '.format(jogo_pc))
print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
print('Você escolheu:  \n{:^33} '.format(jogo_usu))
print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
#comparação
if jogo_pc == 'Pedra' and jogo_usu == 'Pedra':
    print('{:=^40}'.format(' \033[33m EMPATE !!  \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Tesoura' and jogo_usu == 'Tesoura':
    print('{:=^40}'.format(' \033[33m EMPATE !!  \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Papel' and jogo_usu == 'Papel':
    print('{:=^40}'.format(' \033[33m EMPATE !!  \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Pedra' and jogo_usu == 'Papel':
    print('{:=^40}'.format(' \033[34m VOCÊ GANHOU !!! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Papel' and jogo_usu == 'Pedra':
    print('{:=^40}'.format('\033[31m VOCÊ PERDEU !! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Pedra' and jogo_usu == 'Tesoura':
    print('{:=^40}'.format('\033[31m VOCÊ PERDEU !! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Tesoura' and jogo_usu == 'Pedra':
    print('{:=^40}'.format('\033[34m VOCÊ GANHOU !!! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Papel' and jogo_usu == 'Tesoura':
    print('{:=^40}'.format('\033[34m VOCÊ GANHOU !!! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
elif jogo_pc == 'Tesoura' and jogo_usu == 'Papel':
    print('{:=^40}'.format('\033[31m VOCÊ PERDEU !! \033[m'))
    print('=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-')
