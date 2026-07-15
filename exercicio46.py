# Cria uma tupla com os times, imprime a lista completa e 
# depois mostra os 5 primeiros.

# Os 5 primeiros colocados.
# Os últimos 4 colocados.
# Os times em ordem alfabética.
# Em que posição está a Chapecoense (ou outro time, dependendo da lista).

times = ('Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo FC',
         'Santos FC', 'Grêmio', 'Internacional', 'Atlético Mineiro',
         'Cruzeiro', 'Vasco da Gama', 'Botafogo', 'Fluminense',
         'Athletico Paranaense', 'Coritiba', 'Bahia', 'Sport Recife',
         'Fortaleza EC', 'Ceará SC', 'Goiás', 'Vitória')

print(f'Lista de Times: {times}')
print('-=' * 15)

print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)

print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)

print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)

print(f'O Bahia está na {times.index("Bahia") + 1}ª posição.')