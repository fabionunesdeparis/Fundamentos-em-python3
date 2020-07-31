# @Fábio C Nunes - 19.06.20
pessoa = {}
grupo = []
media = 0
lista_mulheres = []
while True:
    #Entrada de dados.
    print('-' * 20)
    print('Cadastro de pessoas')
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    pessoa['sexo'] = sexo
    grupo.append(pessoa.copy())
    pessoa.clear()
    c = ' '
    print('-' * 20)
    while c not in 'SN':
        c = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    if 'N' in c:
        break
print('-' * 20)
#número de pessoas cadastradas.
print(f'A.) {len(grupo)} pessoas foram cadastradas')

#média de idade do grupo.
for i in range(0, len(grupo)):
    media += (grupo[i]['idade'])
media = media / len(grupo)
print(f'B.) A média de idade do grupo cadastrado é igual {media:.2f} anos.')

#Mostrar lista com todas as mulheres.
for i in range (0, len(grupo)):
    if grupo[i]['sexo'] == 'F':
        lista_mulheres.append(grupo[i]['nome'])
print('-' * 20)
print('{:^20}'.format('C.) Lista de Mulheres'))
print('-' * 20)
for i in range(0, len(lista_mulheres)):
    print(lista_mulheres[i])
#Mostrar lista com pessoas com idade acima da média
print('-' * 20)
print('{:^20}'.format('Pessoas acima da média de idade'))
print('-' * 20)
for i in range(0, len(grupo)):
    if grupo[i]['idade'] > media:
        print(f'Nome: {grupo[i]["nome"]:<15}', end = '')
        print(f'Idade: {grupo[i]["idade"]:<15}', end = '')
        print(f'Sexo: {grupo[i]["sexo"]:^2}', end = '')
        print('')
print('-' * 20)
