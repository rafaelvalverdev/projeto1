
QUANTIDADE_DENUMEROS = 4
numeros = []

quantidade_de_noves = 0
posicao_dos_tres = 0
numerospares = []

for n in range(QUANTIDADE_DENUMEROS):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero == 9:
        quantidade_de_noves += 1
    elif numero % 2 == 0:
        numerospares.append(numero)
    elif 3 in numeros:
        posicao_dos_tres = numeros.index(3)
    else:
        posicao_dos_tres = '(Não foi digitado)'

tupla_numeros = tuple(numeros)

print(f'Os números digitados foram: {numeros}')
print(f'A quantidade de "9" digitada foi: {quantidade_de_noves}')
print(f'O primeiro "3" foi digitado na {posicao_dos_tres+1} posição')
print(
    f'A quantidade de números pares digitados foi: {len(numerospares)}')
