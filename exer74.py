from random import randint
#cria a tupla com números aleatórios
numeros = ( randint(0,10), randint(0,10), randint(0,10), randint(0,10),randint(0,10) )
#mostra a tupla gerada
print(numeros)
#mostra o menor e o maior valor da tupla
print(f'O menor valor gerado foi {min(numeros)} e o maior foi {max(numeros)}. ')

#@Fábio C Nunes - 26.05.20
