import random
# Fábio C Nunes
# CRie um programa que sorteie a orde de apresentação de trabalho dos alunos e mostre a ordem sorteada.
# entrada de dados
al1= str(input('Digite o nome do primeiro aluno: '))
al2= str(input('Digite o nome do segundo aluno: '))
al3= str(input('Digite o nome do terceiro aluno: '))
al4= str(input('Digite o nome do quarto aluno: '))
# calculos
lista = ([al1,al2,al3,al4])
# resultado na tela
random.shuffle(lista)
print(lista)





