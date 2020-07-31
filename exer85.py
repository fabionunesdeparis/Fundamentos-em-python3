# @Fábio C Nunes - 06.06.20 ex85
lista = [[],[]]
a = ' '
#entrada de valores, separando em duas listas: par e impar
for i in range(1,8):
    a = int(input(f'Digite o {i}º valor: '))
    if a % 2 == 0:
        lista[0].append(a)
    elif a % 2 != 0:
        lista[1].append(a)
#Adicionando pares e ímpares em uma única lista e ordenando números.
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]} ')
print(f'Os valores ímpares digitados foram: {lista[1]} ')