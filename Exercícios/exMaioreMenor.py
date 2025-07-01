valores = list()
num = 0

for valor in range(0, 6):
    num = int(input("digite um valor: "))
    valores.append(num)

maior = max(valores)
menor = min(valores)
pos_maior = [i for i, x in enumerate(valores) if x == maior]
pos_menor = [i for i, x in enumerate(valores) if x == menor]

print("--"*30)
print(f"Você digitou os valores: {valores} ")
print(f"O maior valor digitado foi {maior} na(s) posição(ões) {pos_maior}")
print(f"O menor valor digitado foi {menor} na(s) posição(ões) {pos_menor}")
