# Exercicio do brasileirao:

brasileirao = (
    "Palmeiras",          # 1º
    "Flamengo",           # 2º
    "Atlético Mineiro",    # 3º
    "Corinthians",        # 4º
    "Fluminense",         # 5º
    "Internacional",      # 6º
    "São Paulo",          # 7º
    "Athletico Paranaense",  # 8º
    "América-MG",         # 9º
    "Botafogo",           # 10º
    "Santos",             # 11º
    "Bragantino",         # 12º
    "Goiás",              # 13º
    "Cuiabá",             # 14º
    "Coritiba",           # 15º
    "Fortaleza",          # 16º
    "Avaí",               # 17º
    "Juventude",          # 18º
    "Ceará",              # 19º
    "Atlético Goianiense"  # 20º
)
# a) os 5 primeiros colocados:
print("-="*20)
print(
    f"Os 5 primeiros colocados do brasileirão foram:\n1º {brasileirao[0]} \n2º {brasileirao[1]} \n3º {brasileirao[2]} \n4º {brasileirao[3]} \n5º {brasileirao[4]}")
print("-="*20)
# b) os 4 ultimos colocados:
print(
    f"os ultimos 4 colocados foram\n20º {brasileirao[19]}\n19º {brasileirao[18]}\n18º {brasileirao[17]}\n17º {brasileirao[16]}")
print("-="*20)
# c) times em odrem ALFABETICA:
print(sorted(brasileirao))
