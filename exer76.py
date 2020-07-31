# @Fábio C Nunes - 26.05.20
#Recebendo nomes e preços dentro da tupla
produtos = ('Lapis','3.00','Caderno','11.99','Caneta','2.25','Borracha','0.50','Apontador','3.45','Cola Tenaz','7.00',
            'Canetinha Colorida','23.00','Caneta Stabilo','5.50','Kit Stabilo','45.99','Apagador','10.00','Lapiseira 0.5','16.90')

print('-' * 60)
print('{:^60}'.format('Listagem de preços'))
print('-' * 60)
for i in range(0, len(produtos)-1 , 2):
    print('{:.<50}'.format(produtos[i]),'R${:>7}'.format(produtos[i+1]))
print('-' * 60)