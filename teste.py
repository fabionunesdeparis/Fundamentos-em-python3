dados = []
pessoas = []
#Cadastro de pessoas na lista
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    print('-' * 30)
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    #validação para continuar
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        print('-' * 30)
    if 'N' in continuar:
        break
#Descobrindo maior e menor peso
maisp = menosp = pessoas[0][1]
for p in pessoas:
    if p[1] > maisp:
        maisp = p[1]
    if p[1] < menosp:
        menosp = p[1]
#Listando as pessoas mais pesadas da lista
print('-' * 30)
print(f'Lista de pessoas mais pesadas com {maisp}kg: ')

for p in pessoas:
    if p[1] == maisp:
        print(p[0])
#Listando as pessoas mais leves da lista
print('-' * 30)
print(f'Lista de pessoas mais leves com {menosp}kg:')
for p in pessoas:
    if p[1] == menosp:
        print(p[0])
#Resultados na tela
print('-' * 30)
print(f'{len(pessoas)} pessoas foram cadastradas')
print('-' * 30)
