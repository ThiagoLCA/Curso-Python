# Crie um programa onde o usuário possa digitar vários números e  
# cadastre-os em uma lista
# a- quantos numeros foram digitados
# b - a lista de valores organizada de forma decrescente. 
# c - se o valor 5 foi digitado e está ou não na lista

numeros= list ()
while True:
    numeros.append (int (input('Digite um numero: ')))
    resposta = str(input(' Quer Continuar? [S/N]'))
    if resposta in 'Nn':
        break

print ('-='*30)

print (f'Você digitou {len(numeros)} Elementos')
numeros