preço = float (input('Qual o preço do Produto? R$ '))
avista = preço - (preço * 10 / 100 )
parcelado = preço + (preço * 5 / 100)
print ('O Produto custa R${}, com pagamento a vista tem 10% de desocnto fica R$ {}, parcelando aumenta  5% ficando R${}'.format(preço, avista, parcelado))