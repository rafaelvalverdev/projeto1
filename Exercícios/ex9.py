numeros = [[], []]
for i in range(0, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

print(
    f'Os numeros pares e impares sao respectivamente {numeros[0]} e {numeros[1]}')
