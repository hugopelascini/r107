# Produit scalaire

nMAx = 3
v1 = []
v2 = []
n = int(input("Entrez la taille des vecteurs (compris entre 1 et 3) : "))
produit_scalaire = 0

while n < 1 or n > nMAx:
    print("Erreur : la taille des vecteurs doit être comprise entre 1 et 3.")
    n = int(input("Entrez la taille des vecteurs (compris entre 1 et 3) : "))

print(f"Saisie du vecteur v1 :")
for i in range(n):
    v1.append(float(input(f"v1[{i}] = ")))

print(f"Saisie du vecteur v2 :")
for i in range(n):
    v2.append(float(input(f"v2[{i}] = ")))

for i in range(n):
    produit_scalaire += v1[i] * v2[i]
print(f"Le produit scalaire de v1 par v2 est : {produit_scalaire}")