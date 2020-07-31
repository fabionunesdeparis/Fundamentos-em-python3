# @Fábio C Nunes - 29.05.20
valores = []
for i in range(0,5):
    v = int(input(f'Digite o  {i + 1}º número: '))
    if i == 0 or v > valores[i-1]:
        valores.append(v)
        print('Valor adicionado no final da lista!')
    else:
      for i in range(0,5):
          if v <= valores[i]:
            valores.insert(i,v)
            print(f'Valor adicionado na posição {i}! ')
            break
print(valores)
