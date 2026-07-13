#crie um programa que leia o ano de nascimento de 7 pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas ja são maiores?

from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))