import moeda

preço = float(input( 'Digite o Preço: R$  '))
print (f'A Metade de {preço} é {moeda.metade(preço)}')
print (f'O Dobro de {preço} é {moeda.dobro(preço)}')
print (f'Aumentando 10% temos: R$ {moeda.aumentar(preço, 10)}')