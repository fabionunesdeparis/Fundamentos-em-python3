from math import trunc

# @Fábio C. Nunes
# Crie um programa que leia um numero real qualquer e mosre na tela apenas a sua porção inteira.

valor = float(input('Digite um valor real: '))
valor2 = trunc(valor)
print('O número {} possui a parte inteira igual a: {}'.format(valor,valor2))