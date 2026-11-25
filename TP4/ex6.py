# Tri de N nombres

tab = [5, 2, 4, 8, 1, 3]
#print(tab)

for i in range(len(tab) - 1):
    indice_min = i

    for j in range(i + 1, len(tab)):
        if tab[j] < tab[indice_min]:
            indice_min = j

    tab[i], tab[indice_min] = tab[indice_min], tab[i]

    print(tab)


# tab = [5, 2, 4, 8, 1, 3]
#print(sorted(tab))
#print(tab)
#[1, 2, 3, 4, 5, 8]
#[5, 2, 4, 8, 1, 3]


#tab = [5, 2, 4, 8, 1, 3]
#tab.sort()
#print(tab)
#[1, 2, 3, 4, 5, 8]