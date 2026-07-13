#mostre a tabuada de um numero que o usuario escolher, 
# só que agora utilzando o laço for

n = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))