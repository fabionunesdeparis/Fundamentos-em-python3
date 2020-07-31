def leiadinheiro(txt=''):
   continua = True
   while continua:
      print(txt, end='')
      a = (input())
      #tratamento se há espaços
      espaços = a.count(' ')
      if espaços > 0:
         print('Digite um valor monetário! Sem espaços!')
         print('-' * 30)
      #tratamento se está vazio
      elif len(a) < 1:
         print('Digite algum valor monetário!')
         print('-' * 30)
      #tratamento se é letra
      elif a.isalpha():
         print('Digite um valor monetário!')
         print('-' * 30)
      else:
         try:
            a = float(a)
            return a
         except:
            print('Digite um valor monetario! Valores alfaneméricos não permitidos!')
            print('-' * 30)
         else:
            continua = False
            a = float(a)
            return a

