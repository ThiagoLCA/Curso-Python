# desafio 104 - Crie um programa com a função leiaint(), que vai funcionar de forma 
# semelhante a função input(), do python. Só que fazendo a validação
# para aceitar apenas um valor numerico. ex: n= leiaint('digite um n')

def leiaInt(msg):
    ok= False
    valor = 0
    while True:
        n= str(input(msg))
        if n.isnumeric():
            valor = int (n)
            ok= True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor

#Programa Principal
n= leiaInt ('Digite um numero: ')
print (f'Você acabou de digitar o numero {n}')
