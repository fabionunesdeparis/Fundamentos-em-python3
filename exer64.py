# @Fábio C Nunes - 18.05.20
num = cont = soma = 0
num = int(input('Digite um valor ou [999] para encerrar: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor ou [999] para encerrar: '))
print('Você digitou {} vezes e a soma entre os valores é: {}'.format(cont, soma))
