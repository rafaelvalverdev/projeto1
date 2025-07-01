lista = ('lapis', 3.0,
         'caneta', 3.50,
         'estojo', 20.0,
         'caderno', 15.0)

for posicao in range(0, len(lista)):
    if posicao % 2 == 0:
        print(f'{lista[posicao]}', end=' ')
    else:
        print(f'{lista[posicao]}')
