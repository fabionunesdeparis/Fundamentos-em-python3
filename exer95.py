# @Fábio C Nunes - 17.06.20
#Variaveis
jogador = dict()
n_partidas = 0
gols = []
time = []
lista = []
continuar = ''
cod = 0

#recebendo dados
while True:
    print()
    print('=-' * 20)
    print('{:^40}'.format('Dados do jogador'))
    print('=-' * 20)
    jogador['nome'] = str(input('Nome: '))
    n_partidas = int(input('Nº de partidas: '))
    if n_partidas == 0:
        print(f'\033[1;31m O jogador {jogador["nome"]} não jogou nenhuma partida e não possui saldo de gols!\033[m')
    else:
        for i in range(0,n_partidas):
            gols.append(int(input(f'Digite o nº de gols da partida {i+1}: ')))
    jogador['qtd_gols'] = gols.copy()
    jogador['total_gols'] = sum(gols.copy())
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()

    continuar = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Valor Inválido!! Digite apenas S/N.')
        continuar = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print()

# Sistema de visualização de detalhes
print('~' * 70)
print('{:<5}   {:<20}   {:^30}   {:>3}'.format('Cód', 'Nome', 'Gols', 'Total'))
print('~' * 70)
for j in range(0, len(time)):
    print('{:<5}   {:<20}   {:^30}   {:>3}'.format(str(j), str(time[j]['nome']), str(time[j]['qtd_gols']), str(time[j]['total_gols'])))
print('~' * 70)

while True:
    cod = int(input('Mostrar dados de qual jogador? [999] para encerrar: '))
    if cod == 999:
        break
    if cod < 0 or cod > len(time):
        print('Valor digitado não corresponde a lista de jogadores. Tente novamente! ')
        print('~' * 70)
    else:
        print()
        print('---> {:^15} {}'.format('Levantamento do jogador', time[cod]['nome']))
        lista = time[cod]['qtd_gols'].copy()
        for i in range (0,len(time[cod]['qtd_gols'])):
            print(f'No jogo {i+1} fez {lista[i]} gols')
        print()
