todosnumeros = []
numerospares = []
numerosimpares = []

while True:
    numero = int(input('Digite um numero inteiro: '))
    todosnumeros.append(numero)
    if numero % 2 == 0:
        numerospares.append(numero)
    else:
        numerosimpares.append(numero)
    continuar = str(input('Deseja continuar? [s/n]'))
    if continuar in 'Nn':
        break


print(f'Os numeros digitados foram: {todosnumeros}')
print(f'Os numeros impares digitados foram: {numerosimpares}')
print(f'Os numeros pares digitados foram: {numerospares}')
