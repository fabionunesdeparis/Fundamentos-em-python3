import math
# @Fábio C. Nunes 05/05/2020
# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

ang_graus = float(input('Digite o valor do angulo: '))
ang_rad = math.radians(ang_graus)
sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tan = math.tan(ang_rad)
print('O angulo {:.2f} possui: \n Seno:{:.2f}\n Cosseno:{:.2f} \n Tangente:{:.2f}'.format(ang_graus,sen,cos,tan))
