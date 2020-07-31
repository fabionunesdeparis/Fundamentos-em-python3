import datetime
# @Fábio C Nunes
ano = int(input('Digite um ano para descobrir se ele é BISSEXTO, para o ano atual digite 0: '))
if ano == 0:
    ano = datetime.date.today().year

if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 100 == 0 and ano %400 == 0):
    print('O ano {} é BiSSEXTO!!!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!!!'.format(ano))