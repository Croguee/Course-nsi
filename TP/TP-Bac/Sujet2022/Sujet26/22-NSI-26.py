#
# Exercice 1
#

def RechercheMin(tab):
    """
    renvoie l'indice de la première occurrence du minimum de ce tableau. Les 
    tableaux seront représentés sous forme de liste
    """
    assert isinstance(tab, list)

    indice = 0
    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            indice =  i
    return indice

assert RechercheMin([5]) == 0
assert RechercheMin([2, 4, 1]) == 2
assert RechercheMin([5, 3, 2, 2, 4]) == 2


#
# Exercice 2
#

def separe(tab):
    i = 0
    j = len(tab)-1
    while i < j :
        if tab[i] == 0 :
            i += 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
