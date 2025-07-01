# Exercicio: programa que leia o ano de nascimento de 7 pessoas e mostre quantas sao maiores de idade e quantas sao menores de idade

import datetime
# Obter o ano atual
ano_atual = datetime.datetime.now().year
# Inicializar contadores
maiores_de_idade = 0
menores_de_idade = 0
# Ler os anos de nascimento

for i in range(7):
    ano_nascimento = int(
        input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade_atual = ano_atual - ano_nascimento
    if idade_atual >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1

print(
    f"O total de pessoas maiores de idade é de {maiores_de_idade} \nJá o total de menores de idade é de {menores_de_idade} pessoas.")
