# @Fábio C Nunes - 25.06.20
def leiaInt(txt=''):
    continua = False
    while continua == False:
        print(txt, end='')
        a = (input())
        if not a.isnumeric():
            print('\033[31mErro! Digite um número inteiro! \033[m')
        else:
            continua = True
    return a


#Main
n = leiaInt('Digite um valoR: ')
print(f'Você acabou de digitar o número {n}')