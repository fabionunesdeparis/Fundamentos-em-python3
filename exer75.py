# @Fábio C Nunes - 26.05.20
#recebendo os valores dentro da tupla
valores = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
           int(input('Digite o terceiro valor: ')), int(input('Digite o último valor: ')))
print(f'Os valores digitados foram: {valores}')

# contando quantas vezes apareceu o 9.
print(f'O número de vezes que o 9 apareceu foi: {valores.count(9)}')

# Em qual posição foi digitado o valor 3.
if 3 in valores:
    print(f'O valor 3 foi digitado pela primeira vez na posição: {valores.index(3)}')
else:
    print('O valor 3 não foi digitado em nenhuma posição! ')

# mostra quais são os numeros pares digitados.
print('Os números pares digitados são: ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end =', ')

