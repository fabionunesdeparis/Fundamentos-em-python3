from datetime import datetime
# @ Fábio C Nunes 12/05/2020
ano = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano
if idade < 18:
    print('Quem nasceu em {} possui {} anos'.format(ano,idade))
    print('faltando \033[34m{}\033[m anos para o alistamento'.format(18-idade))
    print('Seu alistamento será em \033[34m{}\033[m'.format((18-idade) + ano_atual))
elif idade > 18:
    print('Quem nasceu em  \033[31m{}\033[m possui {} anos.'.format(ano,idade))
    print('Deveria ter se alistado a \033[31m{} anos\033[m'.format(idade -18))
    print('Seu alistamento foi em \033[31m{}\033[m'.format((18-idade) + ano_atual))
else:
    print('\033[31mVocê precisa fazer seu alistamento Imediatamente! ')