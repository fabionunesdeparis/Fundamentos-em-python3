# Fábio C Nunes
# Escreva um programa que converta uma temperatura de C. para F.

temperatura = float(input('Qual a temperatura em ºC ? '))
nova = (temperatura * 1.8) + 32
print('A temperatura {:.1f}ºC , corresponde a {:.1f}ºF'. format(temperatura,nova))