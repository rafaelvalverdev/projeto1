x = 0
y = 0
lista = [[], [], [], [], [], [], [], [], []]

for i in range(0, 9):
    valor = int(input(f'Digite um valor para [{x},{y}]'))
    if len(lista) == 0:
        lista.append(valor)
    else:
        lista[i].append(valor)
    if x == 0:
        if y == 0:
            y += 1
        elif y == 1:
            y += 1
        elif y == 2:
            y = 0
            x += 1
    elif x == 1:
        if y == 0:
            y += 1
        elif y == 1:
            y += 1
        elif y == 2:
            y = 0
            x += 1
    elif x == 2:
        if y == 0:
            y += 1
        elif y == 1:
            y += 1
        elif y == 2:
            y = 0
            x == 0

print('-=-'*30)
print(lista[0][0], lista[1][0], lista[2][0])
print(lista[3][0], lista[4][0], lista[5][0])
print(lista[6][0], lista[7][0], lista[8][0])
