# Exercicio de Verificador de SEXO
sexo = str(input("Por favor digite seu SEXO: [F/M]")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite um sexo VÁLIDO, por favor: ')).strip().upper()[0]
print(f'Obrigado, sexo registrado como: {sexo}')
