# @Fábio C Nunes - 07.06.20 Ex86
lista = [[0,0,0], [0,0,0], [0,0,0]]
#Recebendo valores da matriz
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = (int(input('Digite o valor de [{},{}]: '.format(i, j))))
#Mostrando resultados
print('.' * 25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{lista[i][j]:^5}', end='')
    print()
print('.' * 25)
