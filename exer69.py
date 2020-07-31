# @Fábio C Nunes - 19.05.20
ac_dez = 0
cont_masc = 0
cont_m_maior = 0
sexo = ' '
continuar = ' '
print('-' * 20)
print('Cadastre uma pessoa')
while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while continuar not in 'SN':
        print('-' * 20)
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    #teste acima de 18 anos
    if idade >= 18:
        ac_dez += 1
    #teste Homem
    if sexo == 'M':
        cont_masc += 1
    #Teste Mulher acima de 20 anos.
    if sexo == 'F':
        if idade >= 20:
            cont_m_maior += 1
    #teste sair do programa
    if continuar == 'N':
        break
    sexo = ' '
    continuar = ' '
#resultados são apresentados na tela
print(f'{ac_dez} pessoas acima de 18 anos cadastradas.')
print(f'{cont_masc} homens cadastrados.')
print(f'{cont_m_maior} Mulheres acima de 20 anos.')