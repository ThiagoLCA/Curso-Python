# Crie um programa nde o usuário possa digitar vários valores numericos
# Cadastre-os em uma lista. Caso o numero já exista l[a dentro, ele não
# será adicionado. No finalserá exibido todos os valores unicos digitados
# em ordem crescente

numeros = list ()

while True:
    n= int (input('Digite um valor: '))
    if n not in numeros:
        numeros.append (n)
        print ('Valor adicionado com sucesso!....')
    else:
        print ('Valor Duplicado! Não vou adicionar....')
    resposta = input('Quer continuar: [S/N]')
    if resposta in 'Nn':
        break

    print ('-=' *30)
    numeros.sort ()
    print (f'Você digitou os valores: {numeros}')

