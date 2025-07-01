# metodo usando sort():
numeros = list()
while len(numeros) < 5:
    numero = int(input(f"Digite o {len(numeros)+1}º valor único: "))
    if numero in numeros:
        print("O numero digitado já consta na lista")
    else:
        numeros.append(numero)
print("\nNúmeros ordenados:", sorted(numeros))
