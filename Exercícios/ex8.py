pessoas = []
pessoa = []
pessoamaispesada = []
pessoamaisleve = []

while True:
    nome = str(input('Digite o nome: '))
    pessoa.append(nome)
    peso = float(input('Digite o peso: '))
    pessoa.append(peso)

    if len(pessoamaispesada) == 0 and len(pessoamaisleve) == 0:  # Primeira pessoa cadastrada
        pessoamaispesada.append(pessoa[:])
        pessoamaisleve.append(pessoa[:])
    else:  # Compara com o último peso mais pesado
        if peso > pessoamaispesada[-1][1]:
            pessoamaispesada.clear()
            pessoamaispesada.append(pessoa[:])
        elif peso == pessoamaispesada[-1][1]:  # Caso tenha o mesmo peso
            pessoamaispesada.append(pessoa[:])

        if peso < pessoamaisleve[-1][1]:  # Compara com o último peso mais leve
            pessoamaisleve.clear()
            pessoamaisleve.append(pessoa[:])
        elif peso == pessoamaisleve[-1][1]:  # Caso tenha o mesmo peso
            pessoamaisleve.append(pessoa[:])

    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = str(input('Deseja continuar? [s/n]'))
    while continuar not in 'SsNn':
        continuar = str(input('Digite apenas "s" ou "n": '))
    if continuar in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A pessoa mais pesada: {pessoamaispesada}')
print(f'A pessoa mais leve: {pessoamaisleve}')
