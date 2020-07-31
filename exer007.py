# @Fábio Nunes 03/05/2020
# Desenvolva um prorama que leia as duas notas de um aluno e mostre sua média.

nota1 = float(input('Digite qual o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
media = ((nota1+nota2)/2)

print('A nota 1 foi:  {} \n A nota 2 foi: {} \n A média do aluno é: {:.1f}'.format(nota1,nota2,media))