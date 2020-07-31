# @Fábio C Nunes - 23.06.20
from datetime import datetime


def voto(ano):
    ano_atual = datetime.today().year
    global idade
    idade = (ano_atual - ano)
    sit = ''
    if idade < 16:
        sit = 'Não permitido'
    elif idade > 16 and idade < 70:
        sit = 'Obrigatório'
    else:
        sit = 'Opcional'
    return sit


#Main
idade = 0
print('-' * 40)
print('{:^40}'.format('Eleições'))
print('-' * 40)

ano_nascimento = int(input('Digite o ano do seu nascimento: '))
situation = voto(ano_nascimento)
print(f'O eleitor possui  {idade} anos e seu voto é: \033[31m{situation}\033[m')
print('-' * 40)