# @ Fábio C. Nunes 11/05/20
print('-----------------------------------')
print('x-x-x- Empréstimo Bancário -x-x-x')
print('-----------------------------------')
val_casa = float(input('Qual o valor do imovél desejado: R$ '))
salario = float(input('Qual o valor do salário do Comprador: R$ '))
anos = int(input('nº de anos para a quitação:  '))
valor_presta = float(val_casa / (anos * 12))
if valor_presta <= salario * 0.3:
    print('\033[34mO valor da prestação será de: R${:.2f} em {} parcelas\033[m'.format(valor_presta, (anos*12)))
    print('O empréstimo pode ser concedido!')
    print('\033[m-----------------------------------')
else:
    print('\033[31mO financiamento não pode ser executado, o valor da parcela R${:.2f}\nexcede 30% da renda mensal R${:.2f}'.format(valor_presta,(salario * 0.3)))
    print('O empréstimo Não pode ser concedido!')
    print('\033[m-----------------------------------')