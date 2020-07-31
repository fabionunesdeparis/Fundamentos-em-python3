# @ Fábio C Nunes 14.05.20
primeiro_ter = int(input('Digite o 1º termo: '))
razão = int(input('Digite a razão: '))
for i in range(1,11):
    print(primeiro_ter, end=' → ')
    primeiro_ter = primeiro_ter + razão
print('Fim')