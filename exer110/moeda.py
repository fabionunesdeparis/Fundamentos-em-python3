# @Fábio C Nunes - 02.07.20
def aumentar(v, tx, formatado=False):
    valor_aum = v + (v * (tx/100))
    if formatado == False:
        return valor_aum
    else:
        return moeda(valor_aum)


def diminuir(v, tx, formatado=False):
    valor_dim = v - (v * (tx/100))
    if formatado == False:
        return valor_dim
    else:
        return moeda(valor_dim)

def dobro(v, formatado=False):
    dobro = v * 2
    if formatado == False:
        return dobro
    else:
        return moeda(dobro)

def metade(v, formatado =False):
    met = v / 2
    if formatado == False:
        return met
    else:
        return moeda(met)


def moeda(v, moeda='R$'):
    val = f'{moeda} {v:.2f}'
    val = val.replace('.', ',')
    return val


def resumo(valor, dim, aum):
    print('-' * 40)
    print('{:^40}'.format('Resumo do valor'))
    print('-' * 40)
    print(f' Valor analizado: {moeda(valor):>20}')
    print(f' Metade do preço: {metade(valor, True):>20}')
    print(f' Dobro do preço:  {dobro(valor, True):>20}')
    print(f' Preço aumentado: {aumentar(valor, aum,  True):>20}')
    print(f' Preço dimunuido: {diminuir(valor, dim, True):>20}')
    print('-' * 40)





