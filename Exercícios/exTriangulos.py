# Exercício de Análise de Triângulos
r1 = float(input('Iniciando Análise de Triângulos. '
                 'Digite o primeiro lado do triângulo: '))
r2 = float(input('Digite o segundo lado do triângulo: '))
r3 = float(input('Digite o terceiro lado do triângulo: '))
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Os lados formam um triângulo!')

if r1 == r2 == r3:
    print('O triângulo é equilátero!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('O triângulo é isósceles!')
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('O triângulo é escaleno!')
else:
    print('Os lados não formam um triângulo!')
