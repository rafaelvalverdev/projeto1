# Exercício para escrever o numero de 1 a 20 por exteso:

# versao feite na minha tentativa:

# extenso = (
# "zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
# "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")
##
##
# while True:
# numero = int(input('Digite um número no teclado: '))
# if numero in range(0, 21):
# print(f"O numero que voce escreveu foi {extenso[numero]}")
# break
# else:
# print("Número inválido. Por favor tente outra vez.",)

# versao da IA com verificador try-except(nao sabia usar ainda) para erro de valor:
extenso = (
    "zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
    "doze", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    try:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:  # Verifica se está no intervalo válido
            print(f"O número que você escreveu foi {extenso[numero]}")
            break
        else:
            print("Número fora do intervalo. Digite entre 0 e 20.")
    except ValueError:  # Se o usuário digitar algo não numérico
        print("Entrada inválida. Digite apenas números inteiros.")
