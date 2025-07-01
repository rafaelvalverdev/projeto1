pessoas = []
maiorpeso = []
menorpeso = []

while True:
    pessoa = []
    nome = str(input('Nome: ')).strip()
    pessoa.append(nome)
    peso = float(input('Peso: '))
    pessoa.append(peso)
    pessoas.append(pessoa)
    continuar = str(
        input('Gostaria de inserir mais algum número? [s/n] ').strip().lower())
    if continuar != 's':
        break

# Encontrando maiores e menores pesos
maior_peso = menor_peso = pessoas[0][1]
nomes_maior = [pessoas[0][0]]
nomes_menor = [pessoas[0][0]]

for pessoa in pessoas[1:]:
    if pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
        nomes_maior = [pessoa[0]]
    elif pessoa[1] == maior_peso:
        nomes_maior.append(pessoa[0])

    if pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
        nomes_menor = [pessoa[0]]
    elif pessoa[1] == menor_peso:
        nomes_menor.append(pessoa[0])

# Formatando os nomes para exibição


def formatar_nomes(nomes):
    if len(nomes) == 1:
        return nomes[0]
    return ', '.join(nomes[:-1]) + ' e ' + nomes[-1]


# Saídas formatadas
print('-'*30)
print(f'Ao todo, você inseriu {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}kg de {formatar_nomes(nomes_maior)}')
print(f'O menor peso foi de {menor_peso}kg de {formatar_nomes(nomes_menor)}')
