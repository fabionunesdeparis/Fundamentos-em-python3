# @Fábio C Nunes - 19.05.20
while True:
    tabu = int(input('\nQual tabuada deseja visualizar? '))
    if tabu < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{tabu} x {i:^2} = {tabu* i:^3}')