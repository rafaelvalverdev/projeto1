valores = []
while True:
    valor = int(input('Digite um número:'))
    valores.append(valor)
    continuar = str(input('Voce deseja continuar?[S/N] '))
    if continuar.lower() == 'n':
        break

print(f'Os valores digitados foram: {valores}')
print(f'foram digitados {len(valores)} valores')
print(
    f'A lista ordenada de forma decrescente é {sorted(valores, reverse=True)}')

if 5 in valores:
    # Encontra todas as posições onde o 5 aparece
    posicoes = [i for i, x in enumerate(valores) if x == 5]
    print(
        f'O 5 foi digitado {valores.count(5)}x e aparece nas posições: {posicoes}')
else:
    print('O número 5 não foi digitado.')
