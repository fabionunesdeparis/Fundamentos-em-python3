from math import factorial
 # @Fábio C Nunes - 17.05.20

# Maneira 1
# valor = int(input(' Digite um número para calcular seu fatorial: '))
# fatorial = factorial(valor)
# while valor > 1:
#     print(valor, end=' x ')
#     valor -= 1
# print(' = ', fatorial)

# Maneira 2
valor = int(input(' Digite um número para calcular seu fatorial: '))
multiplica = 0
fat = valor
print(valor, '! =', end=' ')
while valor > 1:
    print(valor, end=' x ')
    multiplica = (fat * (valor - 1))
    valor = valor - 1
    fat = multiplica
print('1 = ', fat)