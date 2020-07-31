import random
# @Fábio C Nunes
numero_usu = int(input('Adivinhe um valor de 0 a 5: '))
numero_pc = random.randint(0,5)
print('O número digitado foi: ',numero_usu)
print('O número sorteado foi: ',numero_pc)
if numero_usu == numero_pc:
    print('Voce ganhou!! Parabéns!!!')
else:
    print('Você perdeu!! Desculpe!!!')