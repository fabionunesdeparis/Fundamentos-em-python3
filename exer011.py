# Fábio C Nunes
# Faça um programa que leia  largura e a altura de uma paredeem metros,
# calcule a sua area e a quantidade de tinta necessaria para pinta-la. Sabendo que cada L de tinta pinta uma area
# de dois metros quadrados.

largura = float(input('Digite o valor da largura em metros: '))
altura = float(input('Digite o valor da altura em metros: '))
area = largura*altura
print('O tamanho da parede é de: \n {:.2f}m²'.format(area))
print('Você precisará de: \n {:.2f} Litros de tinta'.format(area/2))


