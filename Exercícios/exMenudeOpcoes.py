# Exercício: ler valores e demonstrar opcoes de operacoes:

n1 = int(input('Digite o promeiro número: '))
n2 = int(input('Digite o segundo número: '))
comando = 0
print('[1] SOMA\n[2] MUTIPLICAÇÃO\n[3] MAIOR NUM\n[4] NOVOS NUMS\n[5] SAIR\n')

while comando != 5:
    comando = int(input('Escolha uma opção: '))
    if comando == 1:
        soma = n1 + n2
        print(f'A SOMA dos valores é: {soma}')
    elif comando == 2:
        mutiplicacao = n1 * n2
        print(f'A mutiplicação entre os valores é {mutiplicacao}')
    elif comando == 3:
        if n1 > n2:
            print(f"O número {n1} é o maior")
        elif n1 < n2:
            print(f"O número {n2} é o maior")
        else:
            print(f"Os números {n1} e {n2} são iguais")
    elif comando == 4:
        n1 = int(input('Digite o novo promeiro número: '))
        n2 = int(input('Digite o novo segundo número: '))
    elif comando == 5:
        print('Saindo...')

    else:
        print('Opção inválida')

print('fim do programa.')
