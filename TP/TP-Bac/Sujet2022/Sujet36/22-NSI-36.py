from math import sqrt   # import de la fonction racine carree

#
# Exercice 1
#

def recherche(tab, n):
    """
    
    """
    assert isinstance(tab, list)
    assert len(tab) != 0
    assert isinstance(n, int)

    indice = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    if indice != None:
        return indice
    else:
        return len(tab)

assert recherche([5, 3],1) == 2
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3



#
# Exercice 2
#

def distance(point1, point2): 
    """ 
    Calcule et renvoie la distance entre deux points. 
    """
    return sqrt((point1[0] - point2[0])**2 + (point1[-1] - point2[-1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ 
    Renvoie le point du tableau tab se trouvant a la plus     
    courte distance du point depart.
    """
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
