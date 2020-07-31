# @Fábio C Nunes - 04.07.20
def leiaInt(txt=''):
    continua = False
    while continua == False:
        print(txt, end='')
        a = input()
        if not a.isnumeric():
            print('\033[31mErro! Digite um número inteiro! \033[m')
        else:
            continua = True
    return a


def leiafloat(txt=''):
    continua = False
    while continua == False:
        print(txt, end='')
        num = input()
        try:
            num = float(num)
        except (ValueError,TypeError):
            print('\033[31mErro! Digite um número real! \033[m')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar esse número!')
            return 0

        else:
            continua = True
    return num


#Main
n = leiaInt('Digite um valor inteiro: ')
m = leiafloat('Digite um valor real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {m}')
