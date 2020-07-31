# @ Fábio C Nunes
contador = 0
num_usu = int(input('Digite um número: '))
for i in range (1,num_usu+1):
    if num_usu % i == 0:
        print('\033[31m',i,'\033[m', end='')
        contador = contador + 1
    else:
        print('\033[33m',i,'\033[m', end='')
print('\nO número {} foi divisivél {} vezes.'.format(num_usu,contador))
if contador != 2:
    print(' Por isso ele não é PRIMO! ')
else:
    print(' Por isso ele é PRIMO! ')
