# @Fábio C Nunes - 18.05.20
soma = maior = menor = numero = int(input('Digite um valor: '))
res = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
cont = 1
while res == 's':
    numero = int(input('Digite um valor: '))
    res = str(input('Deseja continuar? [S/N]')).lower()[0].strip()
    soma += numero
    cont += 1
    #maior e menor
    if maior < numero:
        maior = numero
    elif menor > numero:
        menor = numero
# mostra a média
print('A média entre os valores digitados é: {}'.format(soma/cont))
# mostra o maior e menor
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
