#
# Exercice 1
#

def correspond(mot, mot_a_trous):
    for i in range(len(mot)):
        if mot_a_trous[i] != '*' and mot_a_trous[i] != mot[i]:
            return False
    return True

assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False

#
# Exercice 2
#

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'
    N = len(plan)                          
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True

assert est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}) == False
assert est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}) == True