# @ Fábio C Nunes - 18.05.20
print('*.' * 40)
print('{:^80}'.format('------- Sequência de Fibonacci -------'))
print('*.' * 40)
qd_sequencia = int(input('\nQuantos elementos da sequência deseja visualizar? ')) -1
ant = 1
num = 0
result = 0
print(num, '',end='→ ')
while qd_sequencia > 0:
    result = num + ant
    print(result, '', end='→ ')
    ant = num
    num = result
    qd_sequencia = (qd_sequencia -1)
print(' FIM ')
