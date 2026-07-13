#Faça um programa que mostre a Tabuada de vários Numeros, 
# um de cada vez, para cada valor digitado pelo usuario,
#programa será interrompido quando o numero digitado
#  pelo usuario for negativo

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))

    if n < 0:
        break

    print('-' * 30)

    for c in range(1, 11):
        print(f'{n} x {c:2} = {n * c}')

    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')