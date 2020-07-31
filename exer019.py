import random, math
# @Fábio C. Nunes 05/05/2020
# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome
# deles e escrevendo o nome do escolhido.
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = (aluno1,aluno2,aluno3,aluno4)
print(random.choice(lista))
