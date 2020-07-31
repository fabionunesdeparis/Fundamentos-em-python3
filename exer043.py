# @ Fábio C. Nunes
peso = float(input(' Digite o peso em Kg: '))
altura = float(input(' Digite a altura em Metros: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('O IMC é igual \033[35m{:.1f}\033[m e o individuo está \033[35mABAIXO DO PESO\033[m ideal!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O IMC é igual \033[32m{:.1f}\033[m  e o individuo possui \033[32mPESO IDEAL!\033[m '.format(imc))
elif imc >= 25 and imc < 30:
    print('O IMC é igual \033[33m{:.1f}\033[m e o individuo está com \033[33mSOBREPESO!\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print('O IMC é igual \033[31m{:.1f}\033[m e o individuo possui \033[31mOBESIDADE!\033[m'.format(imc))
else:
    print('O IMC é igual \033[31m{:.1f}\033[m e o individuo possui \033[31mOBESIDADE MORBIDA!\033[m'.format(imc))