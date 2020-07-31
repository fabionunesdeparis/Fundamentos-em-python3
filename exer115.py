# @Fábio C Nunes - 07.07.20
from ex115 import menu
#programa Principal
while True:
    menu.menu()
    opçao = (input('\033[34mSua opção: \033[m')).strip()
    print('-' * 50)
    if opçao.isnumeric():
        op = int(opçao)
        if op == 1:
            menu.ver_pessoas()
        elif op == 2:
            menu.cadastrar_pessoas()
        elif op == 3:
            break
        else:
            print('\033[31mEscolha uma opção válida! Tente novamente! \033[m')
    else:
        print('\033[31mSó serão aceitos números! Tente novamente!  \033[m')

