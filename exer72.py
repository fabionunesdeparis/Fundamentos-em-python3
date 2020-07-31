# @Fábio C Nunes  - 22.05.20
contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num_usu = int(input('Digite um número entre 0 e 20: '))
    if num_usu < 0 or num_usu > 20:
        print('Tente novamente. ', end ='')
    else:
        print(contagem[num_usu])
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
        if continuar == 'N':
            break



