#Programa que pergunte a quantidade de Km percorrido por um carro alugado, quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar sabendo que custa 60,00 por dia e 0,15 centavos por km rodado**

dias = int (input('Quantos dias alugados? '))
km = float (input('Quantos km rodados? '))
pago = dias * 60 + (km * 0.15)
print ('O total a pagar é de R${:.2f}'.format(pago))