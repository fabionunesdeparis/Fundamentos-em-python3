# @Fábio C.  Nunes - 25.06.20
def notas(* tot, sit=False):
    """

    :param tot: É o valor das notas que serão passados como paramêtro
    :param sit: Pode ser True or False, dando a opções de mostrar ou não a situação
    do aluno, podendo ser, ruim para média baixa, Razoavél para medias intermediarias
    ou Ótima para boas medias.
    :return: Retorna um dicionário com: Quantidade de notas, maior e menor nota, média das notas
    e a situação sendo opcional.
    """
    n = dict()
    total = []
    total = tot
    media = sum(total)/ len(total)
    #preenchendo Dicionário com as informações
    n['qtd_notas'] = len(total)
    n['maior_nota'] = max(total)
    n['menor_nota'] = min(total)
    n['média'] = media
    if sit == True:
        if media >= 0 and media < 4:
            n['situação'] = 'Ruim'
        elif media >= 4 and media < 7:
            n['situação'] = 'Razoavél'
        else:
            n['situação'] = 'Ótima'
    aluno = tot
    return n


#Main
r = notas(5.5, 10, 9, 6)
print(r)

