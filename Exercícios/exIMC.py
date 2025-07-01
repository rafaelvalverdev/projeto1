# Exercício de Cálculo de IMC
# IMC = peso(kg) / altura²(metros)
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}')
# Verifica a categoria do IMC
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 24.9:
    print('Você está com o peso normal.')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso.')
elif 30 <= imc < 34.9:
    print('Você está com obesidade grau 1 (moderada).')
elif 35 <= imc < 39.9:
    print('Você está com obesidade grau 2 (severa).')
elif imc >= 40:
    print('Você está com obesidade grau 3 (mórbida).')
else:
    print('Valor inválido.')
