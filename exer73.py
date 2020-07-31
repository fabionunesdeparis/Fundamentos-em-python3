# @Fábio C Nunes - 26.05.20
times = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético Paranaense',
         'São Paulo','Internacional','Corinthians','Fortaleza','Goiás',
         'Bahia','Vasco da GAma','Atletico Mineiro','Fluminense','Botafogo',
         'Ceará','Cruzeiro','CSA','Chapecoense','Avaí',)
#Os cinco primeiros colocados
print('\033[34mOs cinco primeiros colocados:  \033[m')
for c in range(0,5):
    print(f'{c+1}º', times[c])

#Os quatro últimos colocados
print('\n\033[31mOs quatro últimos colocados : \033[m')
cont = -4
pos = 17
for c in range(0,4):
    print(f'{pos}º',times[cont])
    cont += 1
    pos += 1

#Times em ordem alfabética
print('\nTimes em ordem alfabética: ')
print(sorted(times[0:]))

#Localizando a Chapecoense
pos_chape = times.index('Chapecoense')+ 1
print(f'\nA Chapecoense está na {pos_chape}º Posição')

