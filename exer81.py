# @Fábio C Nunes - 30.05.20
valores = []
while True:
    valores.append(int(input(' Digite um valor: ')))
    continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if 'N' in continua:
        break
#mostra a lista em ordem decrescente
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente {valores}')
# O numero de elementos da lista
print(f'O número de elementos cadastrados foi: {len(valores)}')
# Se o número 5 foi cadastrado na lista
if 5 in valores:
    print('O valor 5 foi cadastrado !')
else:
    print('O valor 5 não foi cadastrado !')
