# Exercicio: Programar um jogo de Advinhaçao usando a estrutura de controle WHILE.

import random

print('Sou seu computador e estou pensando em um numero de 0 a 10...')
palpite = int(input('Sera que voce consegue adivinhar? Palpite: '))
numero = random.randint(0, 10)
acertou = 0
while palpite != numero:
    palpite = int(input('Palpite incorreto, tente novamente: '))
    acertou += 1
else:
    print(f'Você acertou na {acertou}ª tentativa!')
