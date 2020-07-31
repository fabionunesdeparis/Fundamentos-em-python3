# @Fábio C Nunes - 09.06.20 ex 89
#Variaveis
aluno = list()
classe = list()
cont = ''
n1 = n2 = media = ''
#Menu
print('-' * 30)
print('{:^30}'.format('Cadastrando média dos alunos'))
print('-' * 30)
#Recebendo dados dentro das listas
while True:
    aluno.append(str(input('Nome  : ')))
    n1 = (float(input('Nota 1:  ')))
    aluno.append(n1)
    n2 = (float(input('Nota 2:  ')))
    aluno.append(n2)
    media = (n1 + n2) / 2
    aluno.append(media)
    classe.append(aluno[:])
    aluno.clear()
    print('-' * 30)
    cont = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    print('-' * 30)
    while cont not in 'SN':
        print('Digite [S/N]!')
        cont = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        print('-' * 30)
    if 'N' in cont:
        break
#mostrando resultados
print('-' * 30)
print('{:^3}     {:^10}     {:^5}'.format('Nº','Nome','Média'))
print('-' * 30)
for i in range(0,len(classe)):
    print(f'{i:^3}     {classe[i][0]:^10}     {classe[i][3]:^5}')
print('-' * 30)
#escolhendo aluno para detalhar notas
ind = int(input('Digite o Nº do aluno para detalhar suas notas ou 999 para encerrar: '))
while True:
    if ind == 999:
        break
    if ind > len(classe):
        print('-' * 30)
        print('Número do aluno inesistente!')
        print('-' * 30)
        ind = int(input('Digite o Nº do aluno para detalhar suas notas ou 999 para encerrar: '))
    else:
        print('-' * 30)
        print(f'As notas de {classe[ind][0]} foram, {classe[ind][1]} e {classe[ind][2]}')
        print('-' * 30)
        ind = int(input('Digite o Nº do aluno para detalhar suas notas ou 999 para encerrar: '))
