# @Fábio C Nunes - 16.06.20
from datetime import date
pessoa = dict()
ano_atual = date.today().year
aposentadoria = 0
#Recebendo dados no dicionário
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = (ano_atual - ano_nasc)
pessoa['ctps'] = int(input('CTPS [Caso não possua, digite 0] : '))
if pessoa['ctps'] != 0:
    ano_contrat = pessoa['ano_contrat'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$  '))
    pessoa['aposentadoria'] = ((ano_contrat + 35) - ano_atual) + pessoa['idade']
#Mostrando dados
print('-' * 20)
print('{:^20}'.format('Dados do cadastro'))
print('-' * 20)
for k, v in pessoa.items():
    print(f'{k} : {v}')
