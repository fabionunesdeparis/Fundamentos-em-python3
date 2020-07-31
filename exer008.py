# @ Fábio C. Nunes 04/05/20
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

valorm = float(input(' Digite um valor em metros: '))
valorkm = (valorm/1000)
valorhm = (valorm/100)
valordam = (valorm/10)
valordc = (valorm*10)
valorc = (valorm*100)
valormil = (valorm*1000)
print ('A medida de {} m é igual: \n {} km \n {} Hm \n {} Dam \n {} dc \n {} cm\n {} mm'.format(valorm, valorkm, valorhm,valordam,valordc,valorc,valormil))