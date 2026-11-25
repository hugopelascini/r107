# Table de multiplication

nombre = float(input("Entrez un nombre pour afficher sa table de multiplication : "))
print(f"Table de multiplication de {nombre} :")

for i in range(1, 11):
    resultat = round(nombre * i,1)
    print(f"{nombre} x {i} = {resultat}")

