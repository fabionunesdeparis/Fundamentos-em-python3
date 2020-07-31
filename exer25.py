# @Fábio C. Nunes 08/05/2020
# Crie um programa que leia o nome completo de uma pessoa e diga se possui 'Silva', em qualquer parte do nome.
nome_completo = str(input('Digite o seu nome completo : ')).strip().lower()
teste = 'silva' in (nome_completo).split()
print('Tem "Silva" em seu nome? ',(teste))