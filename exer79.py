# @Fábio C Nunes - 28.05.20
numeros = []
continuar = ''
cont = 0
localiza = ''
# Recebendo Valores
while True:
    if cont == 0:
        numeros.append(int(input('Digite um valor: ')))
        print('Valor adicionado com sucesso!')
        cont +=1
    elif cont > 0:
        #Comparando se o valor já faz parte da lista
        n = (int(input('Digite um valor: ')))
        localiza = numeros.count(n)
        if localiza == 0:
            numeros.append(n)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor já foi digitado previamente! \n Não adicionado!')
            localiza = ''
    continuar = str(input('Deseja continuar? ')).upper().strip()[0]
    if continuar in 'N':
        break
# Ordenando e exibido valores
numeros.sort()
print('Os valores digitados foram: ', end='')
for i in range(0, len(numeros)):
    print(numeros[i], end=' ')
