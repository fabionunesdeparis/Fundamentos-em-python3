# @ Fábio C Nunes 18.05.20
primeiro_ter = int(input('Digite o 1º termo: '))
razão = int(input('Digite a razão: '))
contador = 10
while contador > 0:
    print(primeiro_ter, end=' → ')
    primeiro_ter = primeiro_ter + razão
    contador -= 1
print('Fim')