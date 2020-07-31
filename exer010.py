# @Fábio C Nunes
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# Conseidere u$ 1,00 = R$3,27


dinheiro = float(input('Quantos reias você tem na carteira: R$'))
emdollar = float(dinheiro/3.27)

print('Você possui \nR${:.2f}\nPode comprar \nU${:.2f} '.format(dinheiro,emdollar))
