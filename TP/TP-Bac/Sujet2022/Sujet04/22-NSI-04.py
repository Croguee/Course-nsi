#
# Exercice 1
# 

def recherche(tab):
    """
    renvoie la liste des couples d'entiers consécutifs
    successifs qu'il peut y avoir dans tab
    """
    result = []
    n = 0
    for i in range(1, len(tab)):
        if tab[n] + 1 == tab[i]:
            result.append((tab[n], tab[i]))
        n += 1
    return result

assert recherche([1, 4, 3, 5]) == []
assert recherche([1, 4, 5, 3]) == [(4,5)]
assert recherche([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert recherche([5, 1, 2, 3, 8, -5, -4, 7]) == [(1, 2), (2, 3), (-5, -4)]

#
# Exercice 2
# 

def propager(M, i, j, val):
    if M[i][j] == val:
        return None

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)

M = [ [0,0,1,0] , [0,1,0,1] , [1,1,1,0] , [0,1,1,0] ]
propager(M,2,1,3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
