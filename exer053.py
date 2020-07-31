# @ Fábio C Nunes
    #recebe o texto do usuario e trata, deixa todas as letras iguais, sem espaços.
frase = str(input('Digite uma frase: ')).lower().strip()
frase2 = frase.replace(' ','')
n_letras = len(frase2)
cont = n_letras-1
invertido = ''
    # atribui o valor invertido a variavel para comparação
for i in range(0, n_letras):
     invertido = invertido + frase2[cont]
     cont = (cont - 1)
    #compara e imprimi o resultado
if frase2 == invertido:
    print('{}\nÉ PALÍNDROMO!!!'.format(frase))
else:
    print('{}\nNÃO É PALÍNDROMO!!!'.format(frase))




