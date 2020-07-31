# @Fábio C Nunes - 27.05.20
valores = []
for i in range(0,5):
    valores.append(int(input(f'Digite o {i+1}º valor para a posição {i} :')))
print('***' * 15)

#descobrindo maior valor
comparador_maior = 0
posição_maior = []
for i in range(0,5):
    if valores[i] > comparador_maior:
        comparador_maior = valores[i]
for i in range(0,5):
    if valores[i] == comparador_maior:
        posição_maior.append(i)

print(f'O maior valor digitado é: {comparador_maior} e sua posição é: {posição_maior}')

#descobrindo o menor valor
comparador_menor = comparador_maior
posição_menor = []
for i in range(0,5):
    if valores[i] < comparador_menor:
        comparador_menor = valores[i]
for i in range(0,5):
    if valores[i] == comparador_menor:
        posição_menor.append(i)

print(f'O menor valor digitado é: {comparador_menor} e sua posição é: {posição_menor}')
print('***' * 15)

