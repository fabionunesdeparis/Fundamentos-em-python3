# @Fábio C Nunes - 24.06.20
def ficha(nome='<Desconhecido>', gols= 0):
    print(f'O Jogador {nome} fez {gols} gols no campeonato.')

#Main
n = str(input('Nome do jogador: '))
gol = str(input('Nº de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if n.strip() == '':
    ficha(gols=gol)
else:
    ficha(n, gol)

