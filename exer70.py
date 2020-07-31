# @Fábio C Nunes 20.05.20
print('--------- Lojas Faban ---------')
total = cont_prod_mil = mais_barato = preço_prod_mais_barato = cont_prod = preço = 0
nome_prod_mais_barato = ' '
while True:
    cont_prod += 1
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    print('--------------------------------')

    #total das compras
    total += preço
    #produtos acima de R$ 1000

    if preço > 1000:
        cont_prod_mil += 1

    # Nome produto mais barato
    if cont_prod == 1 or preço < mais_barato:
        nome_prod_mais_barato = produto
        preço_prod_mais_barato = preço
        mais_barato = preço
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Continuar? S/N: ')).strip().upper()[0]
        print('--------------------------------')
    if continuar == 'N':
        break

print(f'Total das compras R${total}')
print(f'{cont_prod_mil} Produtos acima de R$1000.00.')
print(f'{nome_prod_mais_barato} foi o produto mais barato e custou R${preço_prod_mais_barato}')