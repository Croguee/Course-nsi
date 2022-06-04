P = [2, 5, 10, 50, 100]

def rendu_monnaie(P,x, memo = None, piece = None):
    """
    Détermine le nombre minimal de pièces
    à rendre.

    Algorithme récursif avec mémoïsation.
    P : le jeu de piece
    x : la somme a rendre
    """
    if memo is None:
        memo = {0:0}
    elif piece is None:
        piece = []

    if x == 0:
        return 0

    if x in memo.keys():
        return memo[x]

    nb_min = float('inf')
    piece = []
    for i in P:
        if i <= x:
            nb = 1 + rendu_monnaie(P, x-i, memo, piece)[0]
            if nb <= nb_min:
                nb_min = nb
                memo[x] = nb_min
                piece.append(i)

    return (nb_min, piece)
            

print(rendu_monnaie(P, 171))
