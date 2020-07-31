# @ Fábio C. Nunes 11/05/20
numero = int(input('Digite um número inteiro: '))
print('[1] - Binário\n[2] - Octal\n[3] - Hexadecimal')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    binario = str(bin(numero))
    print('O número digitado {}, convertido para binário é {}'.format(numero, binario[2:]))
elif opcao == 2:
    octal = str(oct(numero))
    print('O número digitado {}, convertido para octal é {}'.format(numero, octal[2:]))
elif opcao == 3:
    hexadecimal = str(hex(numero))
    print('O número digitado {}, convertido para Hexadecimal é {}'.format(numero, hexadecimal[2:]))
else:
    print('\033[31mA opção digitada não consta na lista! ')