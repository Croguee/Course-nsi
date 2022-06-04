#
# Exercice 1
#

def moyenne(liste):
    """
    renvoie la moyenne pondérée d'une liste composée de couples (note, coefficient)
    total_notes : total des notes de la liste
    totals_coefficients : total des coefficients de la liste
    """
    assert type(liste) == list

    total_notes = 0
    total_coefficients = 0
    for i in range(len(liste)):
        total_notes += liste[i][0] * liste[i][1]
        total_coefficients += liste[i][1] 
    return total_notes / total_coefficients

assert moyenne([(15,2),(9,1),(12,3)]) == 12.5

#
# Exercice 2
# 

def pascal(n):
    C = [[1]]
    for k in range(1, n+1):
        Ck = [C[0][0]]
        for i in range(1,k):
            Ck.append(C[k-1][i-1] + C[k-1][i])
        Ck.append(C[0][0])
        C.append(Ck)
    return C

assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]