# @ Fábio C Nunes 18.05.20
print('*.' * 20)
print('{:^40}'.format('Gerador de P.A.'))
print('*.' * 20)
primeiro_ter = int(input('Digite o 1º termo: '))
razão = int(input('Digite a razão: '))
contador = 10
n_termos = 0
while contador > 0:
    print(primeiro_ter, end=' → ')
    primeiro_ter = primeiro_ter + razão
    contador -= 1
    if contador == 0:
        print('Pausa')
        contador = int(input('\nDeseja ver mais quantos termos? '))
        n_termos = n_termos + contador
print('Progressão finalizada com {} termos visualizados.'.format(n_termos))
