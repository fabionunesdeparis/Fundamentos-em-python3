# @Fábio C Nunes 08/05/2020
# CRie um programa que leia uma frase pelo teclado e mostre: - Quantas vezes aparece a letra 'a'
# em qual posição ela aparece a primeira vez e em qual posição ela aparece pela ultima vez.
texto = str(input('Digite um texto: ')).strip().lower()
contador = texto.count('a')
print('(A) aparece: ',contador,'vezes')
contador2 = texto.find('a')
print('(A) aparece primeiro na posição: ',(contador2)+1)
contador3 = texto.rfind('a')
print('(A) aparece por ultimo na posição: ',(contador3)+1)