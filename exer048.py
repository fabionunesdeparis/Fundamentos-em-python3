# @Fábio C Nunes 14.05.20
soma = 0
contador = 0
for c in range(0,501,3):
    print(c)
    if (c % 2 != 0):
        soma = soma + c
        contador = contador + 1
print('A soma de todos os {} números solicitados é igual a {}'.format(contador,soma))