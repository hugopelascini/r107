# Calcul de moyennes

nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0
notes = []

for i in range(nombreEtudiants):
    note = float(input(f"Entrez la note de l'étudiant {i+1} : "))
    if note < 0 or note > 20:
        print("Erreur : la note doit être comprise entre 0 et 20.")
        break
    notes.append(note)
    moyenne += note


nmoyenne = round(moyenne / nombreEtudiants, 2)
print(f"La moyenne de la classe est de {nmoyenne}")
print(f"Numéro de l'étudiant | Note | écart à la moyenne")

for i in range(nombreEtudiants):
    print(f"{i+1} | {notes[i]} | {round(notes[i] - nmoyenne, 2)}")
