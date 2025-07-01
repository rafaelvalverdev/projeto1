# Exercício para programa que leia o primeiro termo e a razao de uma PA para mostrar
# os 10 primeiros termos da progressão.

print('='*20,
      '10 TERMOS DE UMA PA.',
      '='*20)

termo = int(input('Digite o termo: '))
razao = int(input('Agora a razão da progressão: '))
decimo = termo + (10 - 1) * razao

for termo in range(termo, decimo + razao, razao):
    print(f'{termo} -->', end=' ')
