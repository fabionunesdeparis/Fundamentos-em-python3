# @Fábio C Nunes - 18.06.20
def area(a, b):
    total = a * b
    print(f'O terreno possui: {total} m²')


def lin():
    print('~' * 30)


# Main
lin()
print('{:^30}'.format('Area do terreno'))
lin()
area(a=(float(input('Digite a largura [m]: '))), b=(float(input('Digite o comprimento [m]: '))))
lin()
