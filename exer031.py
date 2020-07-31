# @Fábio C Nunes
distancia = float(input('Digite a distancia da viagem em km: '))
if distancia <= 200:
    preco = (distancia * 0.50)
    print('O valor da passagem é de: R${:.2f}'.format(preco))
else:
    preco = (distancia * 0.45)
    print('O valor da passagem é de: R${:.2f}'.format(preco))