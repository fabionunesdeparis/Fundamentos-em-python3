# @Fábio C Nunes - 08.06.20 Ex86
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior = 0
#Recebendo valores da matriz
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = (int(input('Digite o valor de [{},{}]: '.format(i, j))))
#Mostrando matriz na tela e analizando valores
print('.' * 25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'{lista[i][j]:^5}', end='')
        if lista[i][j] % 2 ==0:
            pares += lista[i][j]
        if j == 2:
            coluna3 += lista[i][j]
        if i == 1:
            if lista[i][j] > maior:
                maior = lista[i][j]
    print()
print('.' * 25)
#Mostrando resultados
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é : {coluna3}')
print(f'O maior valor da segunda linha é: {maior}')
