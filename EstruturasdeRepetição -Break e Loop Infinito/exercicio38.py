#Crie um programa que leia o nome e o preço de vários produtos
#O programa deve perguntar se o usuário vai continuar.
# A = No final mostre qual o total gasto na compra
# B = Quantos produtos custam mais de 1000
#C = Qual o nome do produtos mais barato

total = 0
mais_mil = 0
menor_preco = 0
produto_barato = ''

while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))

    total += preco

    if preco > 1000:
        mais_mil += 1

    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome

    continuar = input('Quer continuar? [S/N] ').strip().upper()

    if continuar == 'N':
        break

print('-' * 40)
print(f'Total da compra: R$ {total:.2f}')
print(f'Temos {mais_mil} produto(s) custando mais de R$1000,00.')
print(f'O produto mais barato foi "{produto_barato}", custando R$ {menor_preco:.2f}.')
