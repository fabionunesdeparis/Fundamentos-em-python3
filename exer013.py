# @Fábio C Nunes
# Faça um algoritmo que leia um salário de um funcionário e mostre
# seu salário com novo salário com 15% de aumento

salario = float(input(' Qual o salário do funcionário em reais: R$'))
salario_novo = (salario*0.15) + salario

print('O salário do funcionário reajustado em 15% é de: \nR${:.2f}'.format(salario_novo))