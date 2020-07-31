# @Fábio C Nunes
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
#verificando valor maior
if n1 > n2 and n1 > n3:
    print('O número {} é o maior. '.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior.'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número {} é o maior.'.format(n3))
#verificando valor menor.
if n1 < n2 and n1 < n3:
    print('O número {} é o menor.'.format(n1))
if n2 < n1 and n2 < n3:
    print('O número {} é o menor. '.format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é menor.'.format(n3))