# Exercício de catergoria de natação
import datetime

anodenascimento = int(input("Digite o ano de nascimento: "))
mesdenascimento = int(input("Digite o mês de nascimento: "))
diadenascimento = int(input("Digite o dia de nascimento: "))

# Função para calcular a idade
# A função calcula a idade com base na data de nascimento e na data atual
# NOTA: ainda nao tinha aprendido a usar funções, nao sei se esta é a melhor forma...


def calcular_idade(anodenascimento, mesdenascimento, diadenascimento):
    data_nascimento = datetime.date(
        anodenascimento, mesdenascimento, diadenascimento)
    data_atual = datetime.date.today()
    idade = data_atual.year - data_nascimento.year - \
        ((data_atual.month, data_atual.day) <
         (data_nascimento.month, data_nascimento.day))
    return idade


idade = calcular_idade(anodenascimento, mesdenascimento, diadenascimento)
print(f"Idade: {idade} anos")  # A função retorna a idade em anos
# Verifica a categoria de natação
if idade < 5:
    print("Você não pode competir.")
elif 5 < idade <= 7:
    print("Você está na categoria Mirim")
elif 7 < idade <= 14:
    print("Você está na categoria Infantil")
elif 14 < idade <= 19:
    print("Você está na categoria Junior")
elif 19 < idade <= 25:
    print("Você está na categoria Sênior")
else:
    print("Você está na categoria Master")
