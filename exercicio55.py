# Faça um programa que leia o nome e peso de várias pessoas
# guardadno tudo em uma lista. No final mostre:
# A - Quantas pessoas foram cadastradas
# B - Uma listagem com as pessoas mais pesadas
# C - Uma listgem com as pessoas mais leves

nomes = []
dado = []
maispesados = menospesados = 0

while True:
    dado.append (str (input('Nome: ')))
    dado.append (float (input('Peso: ')))
    if len (nomes) == 0:
        maispesados = menospesados = dado [1]
    else:
        if dado [1] > maispesados:
            maispesados = dado [1]
        if dado [1] <  menospesados:
            menospesados = dado [1]
    nomes.append (dado [:])
    dado.clear ()

    resp = str (input(' Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break 
print ('-=' *30)
print (f'Os dados foram {nomes}')
print (f' Ao todo você cadastrou {len(nomes)} pessoas')
print (f'O Maior peso foi de {maispesados}kg')
for p in nomes:
    if p[1] == maispesados:
        print (f'[{p[0]}]', end = '' )
print (f'O Menor peso foi de {menospesados}kg')
for p in nomes:
    if p[1] == menospesados:
        print(f'[{p[0]}]', end=' ')

