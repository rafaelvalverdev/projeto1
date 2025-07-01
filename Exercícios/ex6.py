expressao = str(input('Digite a expressão: '))
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
    print('A expressao é válida!')
else:
    print('A expressao é inválida.')
