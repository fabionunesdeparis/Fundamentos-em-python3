# @Fábio C Nunes - 10/05/20
a = float(input('Digite o valor do 1º lado: '))
b = float(input('Digite o valor do 2º lado: '))
c = float(input('Digite o valor do 3º lado: '))
#condição
if (b - c) < a < (b + c) or (a - c) < b < (a + c) or (a - b) < c < (a + b):
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas acima NÂO podem formar um triângulo!')