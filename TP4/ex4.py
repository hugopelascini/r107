# Elément le plus fréquent dans une liste

L1 = []
n = int(input("Entrez le nombre d'éléments dans la liste : "))
max = 0
plusfrequent = None

for i in range(n):
    L1.append(input(f"Entrez l'élément {i + 1} : "))

for element in L1:
    count = L1.count(element)
    if count > max:
        max = count
        plusfrequent = element

print(f"L'élément le plus fréquent dans la liste est : {plusfrequent} (apparait {max} fois)")