# Vérification DATE

date = input("Entrez une date (format : jjmmaaaa) : ")
date = list(date)

while int(date[2:4]) < 1 or int(date[2:4]) > 12 or int(date[0:2]) < 1 or int(date[0:2]) > 31:
    print("Erreur : la date doit être au format jjmmaaaa.")
    date = input("Entrez une date (format : jjmmaaaa) : ")
    date = list(date)
while len(date) != 8 or not date.isdigit() :
    print("Erreur : la date doit être au format jjmmaaaa.")
    date = input("Entrez une date (format : jjmmaaaa) : ")
    date = str(date)


print(date)
annee = int(date[4:8])
print(annee)


