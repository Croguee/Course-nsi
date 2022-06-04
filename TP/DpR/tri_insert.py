def tri_insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and k < tab[j]:
            tab[j+1] = tab[j]
            j = j - 1
        tab[j+1] = k
    return tab

# print(tri_insertion([2, 7, 8, 4, 0, 1, 9, 3, 6, 5]))