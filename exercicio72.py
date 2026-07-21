# exercicio 102 - Crie um programa qu tenha uma função fatorial() que receba 2 parametros
# o primeiro que indique o numero a calcular e o outro chamado show 
# que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial

def fatorial (n, show= False):
    """
    -> Calcula o fatorial de um número.
    :Paramametro n = o numero a ser calculado.
    :parametro show: (Opcional), mostrar ou não a conta.
    :return: Retorna o valor do fatorial de um numero n.
    """
    f= 1
    for c in range (n,0,-1):
        if show:
            print (c, end= '')
            if c > 1:
                print (' x ', end= '')
            else:
                print (' = ', end= '')
        f*=c
    return f

#Programa principal
print (fatorial (5, show= True))
help(fatorial)