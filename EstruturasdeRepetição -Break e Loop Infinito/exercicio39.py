#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#nome com todas as leras maiusculas
#nome com todas as letras minusculas
#Quantas letras ao todo sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = input('Digite sem Nome Completo: ').strip()

print('Nome em maiúsculas:', nome.upper())
print ('Nome em Minúsculas: ', nome.lower())
print ('Total de Letras: ', len(nome.replace(' ', '')))
print ('Total de Letras no primeiro nome:', len(nome.split()[0]))