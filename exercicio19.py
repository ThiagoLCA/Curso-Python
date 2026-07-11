alt = float(input( 'Altura da Parede: '))
larg = float (input('Largura da Parede: '))
area = alt *larg
print ('Sua parede tem a dimensão de:{} x {} e sua area é de: {} m².'.format(alt, larg, area))
tinta = area / 2
print ('Para pintar essa parede, você precisará de {} l de tinta.'.format(tinta))
