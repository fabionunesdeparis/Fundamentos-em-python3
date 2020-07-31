# Fábio Nunes
''' Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados'''

numero = int(input('Digite um valor de 0 a 9999: '))
print('O valor digitado possui: ')
numero2 = str(numero+ 10000)
print('O número {}, possui: '.format(numero))
print('Unidade: ',numero2[4])
print('Dezena: ',numero2[3])
print('Centena: ',numero2[2])
print('Milhar: ',numero2[1])

