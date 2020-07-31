# @Fábio C Nunes 16.05.20
#entrada de dados
soma_idade = 0
idade_maior = 0
nome_maior = ''
contador_mulheres = 0
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).lower().strip()
    soma_idade += idade
    if sexo == 'm':
        if idade > idade_maior:
            idade_maior = idade
            nome_maior = nome
    if sexo == 'f':
        if idade < 20:
            contador_mulheres += 1
print('----------------------')
#resultados na tela
media = (soma_idade /4)

print('A média de idade do grupo é de: {} anos'.format(media))
if nome_maior != '':
    print('O nome do homem mais velho é {} e ele possui {} anos.'.format(nome_maior, idade_maior))
else:
    print('Nenhum Homem foi cadastrado!')
if contador_mulheres > 0:
    print('O número de mulheres com menos de 20 anos é: {}'.format(contador_mulheres))
else:
    print('Nenhuma mulher com menos de 20 anos foi cadastrada!')
print('----------------------')
