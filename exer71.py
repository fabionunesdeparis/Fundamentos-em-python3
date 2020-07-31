# @Fábio Nunes - 22.05.20
print('---------- Banco Fabiú ----------')
valor = int(input('Valor a sacar: R$'))
nota_de_um = nota_cinq = nota_vinte = nota_dez = valor_restante = 0
while valor > 0:
        while (valor - 50) > -1:
            valor = valor - 50
            nota_cinq += 1
        if valor == 0:
            break
        else:
            while (valor - 20) > -1:
                valor = valor - 20
                nota_vinte += 1
            if valor == 0:
                break
            else:
                while (valor - 10) > -1:
                    valor = (valor - 10)
                    nota_dez += 1
                if valor == 0:
                    break
                else:
                    while (valor - 1) > -1:
                        valor = valor - 1
                        nota_de_um += 1
                    if valor == 0:
                        break
if nota_cinq > 0:
    print(f'Total de {nota_cinq} cedulas de R$ 50 ')
if nota_vinte > 0:
    print(f'Total de {nota_vinte} cedulas de R$ 20 ')
if nota_dez > 0:
    print(f'Total de {nota_dez} cedulas de R$ 10 ')
if nota_de_um > 0:
    print(f'Total de {nota_de_um} cedulas de R$ 1 ')
