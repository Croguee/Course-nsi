#
# Exercice 1
#

def verifie(tab):
    """
    renvoie True si tab est trié dans l’ordre croissant, False sinon
    """
    assert len(tab) != 0

    for i in range(1, len(tab)):
        if tab[i] < tab[i-1]:
            return False        
    return True


assert verifie([0, 5, 8, 8, 9]) == True
assert verifie([8, 12, 4]) == False
assert verifie([-1, 4]) == True
assert verifie([5]) == True


#
# Exercice 2
#

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale

urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']
assert depouille(urne) == {'B': 4, 'A': 3, 'C': 3}
election = depouille(urne)
assert vainqueur(election) == ['B']
