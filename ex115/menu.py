from time import sleep
def menu():
    print('-' * 50)
    print(f'{"Menu Principal":^50}')
    print('-' * 50)
    print('\033[33m1.\033[m \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2.\033[m \033[34mCadastrar Nova pessoa\033[m')
    print('\033[33m3.\033[m \033[34mSair do sistema\033[m')
    print('-' * 50)


def ver_pessoas():
    #cabeçalho
    print('-' * 50)
    print(f'{"Visualizar Cadastros":^50}')
    print('-' * 50)
    print(f'{"Nome":<40} {"Idade":>3}')
    #lendo arquivo
    people = open ('pessoas.txt', 'r')
    texto = people.read()
    pessoa = texto.split()
    for i in range(0, len(pessoa), 2):
        print(f'{pessoa[i]:<40}{pessoa[i+1]:>3} anos')
    people.close()
    sleep(2)


def cadastrar_pessoas():
    print('-' * 50)
    print(f'{"Cadastrar nova pessoa":^50}')
    print('-' * 50)

    nome = (str(input('Digite o Nome: ')))
    while True:
        idade = (str(input('Digite a idade: ')))
        if idade.isnumeric():
            people = open('pessoas.txt', 'a')
            people.write(nome)
            people.write(' ')
            people.write(idade)
            people.write('\n')
            people.close()
            print('Item cadastrado com sucesso!')
            sleep(2)
            break
        else:
            print('ERRO! Digite um valor numérico!')
