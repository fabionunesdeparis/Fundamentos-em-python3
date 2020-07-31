# @Fábio C. Nunes
# Crie um programa que leia: A.) O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# quantas letras ao todo sem contar espaços
# quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Maiusculas: ',nome.upper())
print('Minusculas: ',nome.lower())
contador = int(nome.count(' '))
nomese = len(nome)
print('nº Letras (sem espaço: {})'.format((nomese - contador)))
pri_nome = (nome.split())
print('nº Letras (1º Nome): ',len(pri_nome[0]))
