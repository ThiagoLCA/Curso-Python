#exercicio 97. Façaum programa que tenha uma função chamada escreva()
#  que receba um texto qualquer como Parametro e mostre uma mensagem com 
# tamanho adaptável

def escreva (msg):
    tam = len(msg) + 4
    print ('~'* tam)
    print (f'  {msg}')
    print ('~'* tam)

# Programa Principal

escreva ('Thiago Araújo')
escreva ('Milionário')
escreva ('Marketing Digital')
