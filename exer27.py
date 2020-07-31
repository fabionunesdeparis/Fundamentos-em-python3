# @ Fábio C Nunes 08/05/2020
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome.
n_completo = str(input('Digite seu nome completo: ')).strip()
lista = (n_completo).split()
print('Seu primeiro Nome é: ', lista[0])
i = len(lista)-1
print('Seu último nome é: ',lista[i])
