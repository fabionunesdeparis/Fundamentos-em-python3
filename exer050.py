# @Fábio C Nunes 14.05.20
soma = 0
num_usu = 0
for i in range(1, 7):
    num_usu = int(input('Digite um número inteiro: '))
    if (num_usu % 2) == 0:
        soma += num_usu
print('O total da soma de números pares é de: {}'.format(soma))

