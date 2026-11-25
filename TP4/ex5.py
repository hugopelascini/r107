# Vérification DATE

date = input("Entrez une date (format : jjmmaaaa) : ")
date = list(date)
#print(date)

if len(date) != 8:
    print("Erreur : la date doit être au format jjmmaaaa.")
for i in range(len(date)):
    if not date[i].isdigit():
        print("Erreur : la date doit être au format jjmmaaaa.")
        break


