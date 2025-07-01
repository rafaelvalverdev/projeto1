# Exercicio para verificar se a frase ou a palavra é um palíndromo

# Retira os espaços em branco e transforma tudo em minusculo
frase = str(input("Digite uma frase/palavra: ")).strip().lower()
palavra = frase.split()  # Separa a frase em palavras
junto = ''.join(palavra)  # Junta as palavras sem espaços
inverso = junto[::-1]  # Inverte a string
print(inverso)
if inverso == junto:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
