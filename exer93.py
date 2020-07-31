# @Fábio C Nunes - 17.06.20
#Variaveis
jogador = dict()
n_partidas = 0
gols = []
#recebendo dados
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
jogador['qtd_gols'] = gols
jogador['total_gols'] = sum(gols)

# mostrando na tela maneira 1.
print('=-' * 20)
print(jogador)
print('=-' * 20)
# mostrando na tela maneira 2.
print('=-' * 20)
for k, v in jogador.items():
    print(f'O Campo {k} tem o valor: {v}')
print('=-' * 20)
# mostrando na tela maneira 3
print('=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {n_partidas} partidas.')
for i in range(0,n_partidas):
    print(f'Na partida {i+1} fez: {gols[i]} gols.')