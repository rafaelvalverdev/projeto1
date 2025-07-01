numero = int(input("Digite o número que deseja\ncalcular seu FATORIAL: "))
i = 1
fatorial = 1

while i <= numero:
    fatorial = fatorial * i
    i += 1

print(f"O fatorial de {numero} é {fatorial}")
