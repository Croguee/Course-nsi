def rendu_monnaie(P,x):
    """
    P : la liste des pièces disponibles
    x : le montant à rendre
    Retourne le nombre minimal de pièces à rendre
    """
    # cas d'arrêt
    if x == 0:
        return 0
    # On initialise le minimum à l'infini
    nb_min = float('inf')
    
    # cas général
    for i in P:
        if i <= x:
            nb = 1 + rendu_monnaie(P, x-i)
            if nb < nb_min:
                # affectation de la nouvelle valeur mini dans nb_min
                nb_min = nb
    # On retourne le nombre mini trouvé
    return nb_min