#Fábio C. Nunes 08/05/2020
velocidade = float(input('Digite a velocidade do veículo: '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO!!!')
    valor = float(velocidade-80)*7
    print('O valor da multa é de R${} reais'.format(valor))
else:
    print('Você está dirigindo dentro do limite, PARABÉNS')