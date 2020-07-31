# @Fábio C Nunes - 22/06/20
def escreva(txt1, txt2, txt3):
    texto = [txt1, txt2, txt3]
    tamanho = [len(txt1), len(txt2), len(txt3)]
    for i in range(0,len(texto)):
        print('~' * (tamanho[i] + 2))
        print(texto[i])
        print('~' * (tamanho[i] + 2))


#Main
escreva(str(input('Digite o 1º texto: ')), str(input('Digite o 2º texto: ')), str(input('Digite o 3º texto: ')) )