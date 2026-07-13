#crie um programa que leia o nome de uma cidade e 
# diga se ela começa ou não com a palavra santo

cidade = input ('Digite o nome de uma cidade: ').strip()
print(cidade[:5].upper() == 'SANTO')