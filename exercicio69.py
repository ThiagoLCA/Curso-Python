# Faça um programa que tenha uma função chamada contador()
# que receba 3 parametros: inicio, fim e passo. 
# Seu programa tem que realizar 3 contagens a partie da função criada:
# A - de 1 até 10 de um em um. 
# B - de 10 até 0 de 2 em 2. 
# C - Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print ('-=' *20)
    print (f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep (2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print (f'{cont}', end= '', flush = True)
            sleep (0.5)
            cont += passo
        print ('FIM')
    else: 
        cont =1
        while cont >= fim:
            print (f'{cont}', end= '', flush = True)
            sleep (0.5)
            cont -= passo
    print ('FIM')
    
# Programa Principal

contador (1,10,1)
contador (10,0,2)
print ('-=' *20)
print ('Agora é sua vez de personalizar a contagem!')
ini = int(input('INICIO'))
fi = int (input('FIM'))
pa = int (input ('PASSO'))
contador (ini, fi, pa)