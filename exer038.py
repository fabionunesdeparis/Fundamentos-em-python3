# @ Fábio C Nunes 12/05/20
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O número {} é maior que {} '.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que {} '.format(n2, n1))
else:
    print('Os números\033[31m {}\033[m e \033[31m{} \033[msão iguais! '.format(n1, n2))