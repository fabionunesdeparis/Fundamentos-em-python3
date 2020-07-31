# @Fábio C Nunes
print('=-=-==--=-=- Lojas Fábio -=-=-=-=-=-=')
valor_compra = float(input('Digite o valor da compra: '))
print('''
[1] - À Vista 
[2] - À Vista no cartão
[3] - 2x Cartão
[4] - 3x ou mais no cartão
''')
opcao = int(input(' Digite a sua opção: '))
if opcao == 1:
    valor_final = valor_compra - (valor_compra * 0.10)
    print('À vista em dinheiro')
    print('Valor da compra: R${:.2f}'.format(valor_compra))
    print('Valor do desconto: R${:.2f}'.format(valor_compra * 0.10))
    print('TOTAL a pagar: R${:.2f}'.format(valor_final))
elif opcao == 2:
    valor_final = valor_compra - (valor_compra * 0.05)
    print('À vista no cartão')
    print('Valor da compra: R${:.2f}'.format(valor_compra))
    print('Valor do desconto: R${:.2f}'.format(valor_compra * 0.05))
    print('TOTAL a pagar: R${:.2f}'.format(valor_final))
elif opcao == 3:
    valor_final = valor_compra
    print('2x no cartão')
    print('Valor da compra: R${:.2f}'.format(valor_compra))
    print('Valor do desconto: R${:.2f}'.format(0))
    print('Valor da parcela: R${:.2f}'.format(valor_final / 2))
    print('TOTAL a pagar: R${:.2f}'.format(valor_final))
elif opcao == 4:
    n_parcelas = int(input('Digite o número de parcelas: '))
    valor_final = (valor_compra * 0.20) + valor_compra
    print('{} x no cartão'.format(n_parcelas))
    print('Valor da compra: R${:.2f}'.format(valor_compra))
    print('Valor do juros: R${:.2f}'.format(valor_compra * 0.20))
    print('Valor da parcela: R${:.2f}'.format(valor_final / n_parcelas))
    print('TOTAL a pagar: R${:.2f}'.format(valor_final))
else:
    print('Opção inválida! Digite um valor entre 1 e 4. ')

