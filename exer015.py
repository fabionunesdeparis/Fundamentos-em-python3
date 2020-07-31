# @Fábio C. Nunes
# Escreva um programa que pergunte a quantidade de quilometros percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que
# O carro custa R$60,00 por dia e R$0,15 por km rodado.

km = float(input('Quilometros percorridos pelo carro: '))
dias = int(input('Dias de aluguel do veículo: '))
valor_a_pagar = (dias * 60)+(km *0.15)
print('O valor a ser pago é de: R$ {:.2f}'.format(valor_a_pagar))

