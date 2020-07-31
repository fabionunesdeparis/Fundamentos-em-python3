# @Fábio C NUnes
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
cidade = str(input('Escreva o nome da cidade: ')).lower().strip()
i = 'santo' in (cidade)
y = ' ' in (cidade[5])
z = i and y == True
print(z)
