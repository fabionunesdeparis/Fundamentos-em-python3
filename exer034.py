# @Fábio C Nunes 10/05/2020
print('xxx---' * 5)
salario = float(input('Qual o salário do funcionário: '))
teto = 1250
if salario <= teto:
    salarioatual = (salario * 0.15) + salario
else:
    salarioatual = (salario * 0.10) + salario
print('O novo salário do funcionário será de: R${} '.format(salarioatual))
print('xxx---' * 5)