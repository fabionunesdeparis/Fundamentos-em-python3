# @Fábio C Nunes - 31.05.20
numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if 'N' in continua:
        break
print(f'Todos os valores digitados foram: {numeros}')
print(f'Todos os valores pares foram: {pares}')
print(f'Todos os valores ímpares foram: {impares}')
