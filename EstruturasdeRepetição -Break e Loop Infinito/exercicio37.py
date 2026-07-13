#Crie um programa que leia a idade e o sexo de varias pessoas
#A cada pessoa cadastrada, o programa deve perguntar 
# se o usuario quer ou não continuar. No final mostra: 
# A = Quantas pessoas tem mais de 18 anos
# B = Quantos homens foram cadastrados
# C = Quantas mulheres tem menos de 18 anos

maiores = 0
homens = 0 
mulheres_menores = 0 

while True:
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str (input ('Sexo [M/F]: ')).strip () .upper () [0]

    if  idade >=18:
        maiores +=1
    
    if sexo == 'M':
        homens  += 1

    if sexo == 'F' and idade < 18:
        mulheres_menores += 1

    continuar = input ('Quer continuar? [S/N] ') .strip (). upper ()

    if continuar == 'N':
        break

print ('-' *30)
print (f'Total de Pessoas com mais de 18 anos {maiores}')
print (f'Ao todo temos {homens} homens cadastrados')
print (f'E temos {mulheres_menores} mulheres com menos de 18 anos')