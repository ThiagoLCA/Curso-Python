#Faça um programa que jogue par ou ímpar com o computador
#O JOgo só será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas que ele conquistou 
# no final do jogo

from random import randint

vitorias = 0



while True:
    jogador = int(input('Digite um valor '))
    computador = randint (0, 10)
    total = jogador + computador

    escolha = input ('Par ou Impar? P/I') .strip().upper()

    print ('-' *30)
    print (f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    
    if total %2 == 0:
        print ('Deu par')
    else:
        print ('Deu ìmpar')

    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break

    print('-' * 30)

print('-' * 30)
print(f'GAME OVER! Você venceu {vitorias} vezes consecutivas.')