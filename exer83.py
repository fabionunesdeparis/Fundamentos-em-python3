# @Fábio C Nunes - 31.05.20
print('--' * 30)
print('{:^60}'.format('Analizador de Expressões'))
print('--' * 30)
a = str(input('Digite sua expressão: '))
contadora = a.count('(')
contadorf = a.count(')')
prim_parentese_abre = a.index('(')
prim_parentese_fecha = a.index(')')

#analisando o numero de parenteses e analisando a ordem dos parenteses
if contadora == contadorf and prim_parentese_abre < prim_parentese_fecha:
    print('Sua expressão é valida!')
else:
    print('Sua expressão é ínvalida')



