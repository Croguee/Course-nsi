#
# Exercie 1
#

def indice_du_min(tab):
    nb_min = tab[0]
    index = 0
    for i in range(1, len(tab)):
        if nb_min > tab[i]:
            index = i
            nb_min = tab[i]
    return index

#
# Exercice 2
#

def separe(tab):
    i = 0
    j = len(tab) -1
    while i < j :
        if tab[i] == 0 :
            i += 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j -= 1
    return tab