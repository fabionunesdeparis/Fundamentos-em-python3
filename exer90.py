# @Fábio C Nunes - 14.06.20
classe = {}
n = str(input('Digite o nome do aluno : '))
m = float(input('Digite a média do aluno: '))
if m > 7:
    sit = 'Aprovado!'
else:
    sit = 'Reprovado!'
classe['nome'] = n
classe['média'] = m
classe['situação'] = sit
print('*' * 30)
print(f'O aluno(a) {classe["nome"]} tirou {classe["média"]} e sua sitação é: {classe["situação"]}')

