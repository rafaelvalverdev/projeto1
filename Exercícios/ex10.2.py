matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha},{coluna}]'))

print('\nMatriz 3x3:')
print('-=' * 20)
for linha_index, linha_valores in enumerate(matriz):
    for coluna_index, elemento in enumerate(linha_valores):
        # :^5 centraliza o número em 5 espaços
        print(f'[{elemento:^5}]', end='')
        if elemento % 2 == 0:
            soma_pares += elemento
        if coluna_index == 2:
            soma_terceira_coluna += elemento
    if linha_index == 1:
        maior_valor_segunda_linha = max(linha_valores)

    print()  # Nova linha após cada linha da matriz
print('-=' * 20)
print(f'A soma dos valores pares é {soma_pares} ')
print(f'A soma dos valores da terceira coluna é : {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
