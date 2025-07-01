palavras = (
    "casa", "gato", "livro", "sol", "agua",
    "tempo", "flor", "noite", "dia", "rua",
    "pai", "mae", "amigo", "porta", "cadeira",
    "mesa", "vida", "cor", "sonho", "verde"
)
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    vogais_presentes = []  # Lista para armazenar as vogais da palavra atual
    for letra in palavra:
        if letra in vogais and letra not in vogais_presentes:  # Evita repetições
            vogais_presentes.append(letra)
    print(
        f'Na palavra "{palavra.upper()}" temos as vogais: {", ".join(vogais_presentes)}')
