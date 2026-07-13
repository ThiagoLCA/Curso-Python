#desenvolva um programa que leia 6 numeros inteiros e mostre a soma 
# apenas dos que forem pares. Se for impar, desconsiderar.

soma = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))

    if n % 2 == 0:
        soma += n

print('A soma dos números pares é {}'.format(soma))