import random

def generer_pyramide(h):
    """
    Retourne une pyramide de hauteur h contenant des nombres aléatoires entre 1 et 9
    """
    pyramide = []
    for lenght in range(h):
        pyramide.append([random.randint(1,9) for i in range(lenght+1)])
    return pyramide
    

def afficher_pyramide(p):
    """
    Affiche la pyramide p
    """
    for i in p:
        espaces = (len(p) - len(i))*' '
        affichage = espaces + ' '.join([str(v) for v in i])
        print(affichage)


def sous_pyramide_gauche(p):
    return [line[:-1] for line in p if len(line) > 1]

def sous_pyramide_droite(p):
    return [line[1:] for line in p if len(line) > 1]

def recherche_max_brute(p):
    """
    Recherche du chemin optimal parmi tous les chemins possibles
    """
    sommet = p[0][0]
    if len(p) == 1:
        return sommet
    
    pyramide_gauche = sous_pyramide_gauche(p)
    pyramide_droite = sous_pyramide_droite(p)
    return sommet + max(recherche_max_brute(pyramide_gauche), recherche_max_brute(pyramide_droite))


def build_max_pyramide(p, line=0):
    """
    Retourne la pyramide p_max ( p est modifiée 'in place' )
        4               4
       9 1            13 5
      1 2 9    =>    14 15 14
     1 7 9 1        15 22 24 15
    line : le numéro de ligne
    """
    # Si on ne se trouve pas au sommet
    if line != 0:
        # Pour la première case de la ligne courante, on ajoute la première case de la ligne du dessus
        p[line][0] += p[line-1][0]
        # Pour la dernière case de la ligne courante, on ajoute la dernière case de la ligne du dessus
        p[line][-1] += p[line-1][-1]
        # On parcourt toutes les autres cases et on y ajoute le plus grand contenu des deux cases supérieures
        for i in range(1,line):
            p[line][i] += max(p[line-1][i-1], p[line-1][i])
            
    # Cas général : nous ne sommes pas à la dernière ligne 
    if line < len(p) - 1:
        return build_max_pyramide(p, line+1)
    # Cas d'arrêt : on est arrivé à la dernière ligne
    else:
        return p
    
def Build_max_pyramide(p):
    """
    Retourne la pyramide p_max ( p est modifiée 'in place' )
        4               4
       9 1            13 5
      1 2 9    =>    14 15 14
     1 7 9 1        15 22 24 15
    line : le numéro de ligne
    """
    for line in range(1, len(p)):
        # Gauche
        p[line][0] += p[line-1][0]
        # Droite
        p[line][-1] += p[line-1][-1]
        # Element au milieu
        for i in range(line):
            p[line][i] += max(p[line-1][i-1], p[line-1][i])

    return p
        
def get_max_value(p):
    return max(p[-1])
    # retourne la valeur maximale de la dernière ligne



pyramide = generer_pyramide(4)
gwosse_pywamide = generer_pyramide(20)
afficher_pyramide(pyramide)

# afficher_pyramide(pyramide)
# afficher_pyramide(sous_pyramide_gauche(pyramide))
# afficher_pyramide(sous_pyramide_droite(pyramide))
# recherche_max_brute(gwosse_pywamide)

afficher_pyramide(Build_max_pyramide(pyramide))
print(get_max_value(p))