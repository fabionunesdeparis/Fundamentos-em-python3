# @Fábio C Nunes - 30.06.20
def aumentar(v, formatado=False):
    valor_aum = v + (v * 0.1)
    if formatado == False:
        return valor_aum
    else:
        return moeda(valor_aum)


def diminuir(v, formatado=False):
    valor_dim = v - (v * 0.1)
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


def moeda(valor, moeda='R$'):
    val = f'{moeda} {valor:.2f}'
    val = val.replace('.', ',')
    return val

