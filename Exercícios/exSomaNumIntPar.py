# Exercício para soma de 6 numeros inteiros considerando apenas os pares

soma = 0
contador = 0

for numero in range(1, 7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print(f'a soma dos {contador} valores pares informados é: {soma}')
