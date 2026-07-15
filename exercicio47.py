# Faça um programa que leia 5 valores numericos 
# e guarde-os em uma lista. Mostre qual foi o maior e
#  o menor valor digitado e suas respectivas posições na lista

lista = []

for i in range(0,5):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    lista.append(valor)

maior = max(lista)
menor = min(lista)

print('-=' * 20)
print(f'Você digitou os valores: {lista}')

print(f'O maior valor foi {maior}, nas posições: ', end='')
for pos, valor in enumerate(lista):
    if valor == maior:
        print(pos, end=' ')

print()

print(f'O menor valor foi {menor}, nas posições: ', end='')
for pos, valor in enumerate(lista):
    if valor == menor:
        print(pos, end=' ')