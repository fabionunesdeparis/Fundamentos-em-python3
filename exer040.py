# @ Fábio C. Nunes
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Aluno \033[31m REPROVADO!\033[m  sua média foi: \033[31m {}\033[m '.format(media))
elif media >= 5 and media <= 6.9:
    print('Aluno em \033[33mRECUPERAÇÃO!\033[m  sua média foi: \033[33m {}\033[m '.format(media))
else:
    print('Aluno \033[34m APROVADO!\033[m sua média foi: \033[34m{}\033[m'.format(media))