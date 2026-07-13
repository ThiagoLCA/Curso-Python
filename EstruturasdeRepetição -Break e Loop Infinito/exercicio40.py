#Faça um programa que leia de 0 a 9999e mostre na tela cada um 
#um dos dígitos separados - unidade, dezena, centena e milhar

numero = int(input('Digite um número entre 0 e 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
