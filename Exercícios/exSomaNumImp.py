# Programa que calcula a SOMA entre numeros IMPARES MULTIMPOS DE 3 entre 1 e 500

soma = 0  # Inicializa a variável soma com 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
print(f'A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {soma}')
