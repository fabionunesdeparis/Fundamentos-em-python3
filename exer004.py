# lê dados
tela = str(input('Digite algo: '))

# testa dados
tipo = (type(tela))
a = (tela.isalnum())
b =(tela.isalpha())
c = (tela.islower())
d = (tela.isupper())
e = (tela.istitle())
# resultados
print('O usuário digitou: {}'.format(tela))
print('O tipo primitivo é: {}'.format(tipo))
print('O valor é alfa-numerico: {}' .format(a))
print('O valor é composto por caracteres apenas:{}'.format(b))
print('O valor é minusculas: {}'.format(c))
print('O valor é maiusculas: {}'.format(d))
print('Está capitalizada: {}'.format(e))