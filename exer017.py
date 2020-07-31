from math import sqrt
''' @ Fábio C Nunes 05/05/2020
Faça um programa que leia um comprimento do cateto, do cateto adjacente de um triangulo retangulo
calcule e mostre o comprimento da hipotenusa.
'''

catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto Adjacente: '))
hiposqt = pow(catop,2)+pow(catadj,2)
hipo = sqrt(hiposqt)

print('Hipotenusa é igual: {:.2f}'.format(hipo))
