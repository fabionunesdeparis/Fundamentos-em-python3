# @Fábio C Nunes 19.05.20
cont = soma = 0
while True:
    num = int(input('Digite um número ou 999 para encerrar: '))
    if num == 999:
        break
    else:
        cont += 1
        soma += num
print(f'{cont} números foram digitados e a soma entre eles é: {soma}')
