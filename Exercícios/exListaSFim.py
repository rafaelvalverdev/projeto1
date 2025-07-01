# digitar valores numericos para cadastrar na lista
# nao pode duplicar o numero na lista
# exibir no final os valores em ordem crescente.

numeros = list()

while True:
    num = int(input('Digite um número inteiro para inserir na lista: '))
    if num not in numeros:   # Verifica se o número já está na lista antes de adicionar
        numeros.append(num)
        print('O valor foi adicionado à lista...')
    else:   # Pergunta se deseja continuar
        print('Valor duplicado! Não será adicionado.')
    continuar = str(
        input('Gostaria de inserir mais algum número? [s/n] ').strip().lower())
    if continuar != 's':
        break

print()
numeros = sorted(numeros)
print('\nVocê digitou os valores:', numeros)
