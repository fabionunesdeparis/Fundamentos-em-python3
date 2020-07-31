# @Fábio C Nunes 16.05.20
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = menor = peso
    elif maior <= peso:
        maior = peso
    elif menor >= peso:
        menor = peso
print('O menor peso foi: {} '.format(menor))
print('O maior peso foi: {} '.format(maior))
