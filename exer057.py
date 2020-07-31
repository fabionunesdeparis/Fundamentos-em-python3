# @Fábio C Nunes - 16.05.20
sexo = str(input('Sexo M/F: ')).upper()[0].strip()
while sexo not in 'MF':
    print('Digite Novamente')
    sexo = str(input('Sexo M/F: ')).upper()[0].strip()
print('Sexo registrado com sucesso! ')