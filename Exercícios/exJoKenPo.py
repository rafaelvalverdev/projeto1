# Jogo de Jokenpô
import time
import random
print('-'*20, 'Jokenpô', '-'*20)
# Definindo as opções do jogo
opcoes = ['pedra', 'papel', 'tesoura']
# Solicita a escolha do jogador
jogador = input('Escolha pedra, papel ou tesoura: ').lower().strip()
# Verifica se a escolha do jogador é válida
if jogador not in opcoes:
    print('Escolha inválida!')
else:
    # Gera a escolha do computador
    computador = random.choice(opcoes)
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ!')
    time.sleep(1)
    print(
        f'-------------------------------\n O computador escolheu: {computador} \n-------------------------------')
    # Verifica o resultado do jogo
    if jogador == computador:
        print('Empate!')
    elif (jogador == 'pedra' and computador == 'tesoura') or \
            (jogador == 'papel' and computador == 'pedra') or \
            (jogador == 'tesoura' and computador == 'papel'):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
# Fim do jogo
