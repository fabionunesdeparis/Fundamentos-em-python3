# @Fábio C. Nunes
# Faça um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

preco = float(input('Digite o valor do produto: R$ '))
ind = (5 / 100)
desconto = (preco * ind)

print('O Valor sem desconto é de: R$ {}\nO valor com Desconto é de: R$ {}'.format(preco,preco-desconto))