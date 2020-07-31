from datetime import datetime
# @Fábio C Nunes
contador_maior = 0
contador_menor = 0
ano_atual = datetime.today().year
for i in range(1,8):
    ano_nasc = int(input(' Em que ano a {}ª pessoa nasceu? '.format(i) ))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        contador_maior += 1
    else:
        contador_menor += 1
print('Número de pessoas maiores: {}'.format(contador_maior))
print('Número de pessoas menores: {}'.format(contador_menor))



