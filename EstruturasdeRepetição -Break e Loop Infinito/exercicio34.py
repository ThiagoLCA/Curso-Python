#Crie um programa que leia vários numeros inteiros pelo teclado. 
#O Programa só vai parar quando o usuario digitar 999 
# que é a condição de parada. No final, mostre quantos numeros foram 
#digitados e qual a soma entre eles. Desconsiderando o flag

soma = 0
contador = 0

n = int(input('Digite um número [999 para parar]: '))

while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números.'.format(contador))
print('A soma entre eles foi {}.'.format(soma))