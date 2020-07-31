from datetime import datetime# @ Fábio C Nunes 12/05/20
ano_nascimento = int(input(' Digite o ano de nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('O atleta possui {} anos e sua categoria é Mirim'.format(idade))
elif (idade > 9) and (idade <= 14):
    print('O atleta possui {} anos e sua categoria é infantil'.format(idade))
elif (idade > 14) and (idade <= 19):
    print('O atleta possui {} anos e sua categoria é Junior'.format(idade))
elif (idade > 19) and (idade <= 25):
    print('O atleta possui {} anos e sua categoria é Sênior'.format(idade))
else:
    print('O atleta possui {} anos e sua categoria é Master'.format(idade))


