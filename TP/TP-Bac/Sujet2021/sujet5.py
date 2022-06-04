#
# Exercice 1
#

def convertir(T):
    """
    T est un tableau d'entiers, dont les éléments sont 0 ou 1 et
    représentant un entier écrit en binaire. Renvoie l'écriture
    décimale de l'entier positif dont la représentation binaire
    est donnée par le tableau T
    """
    index = []
    result = 0
    for i in range(len(T)):
        if T[i] == 1:
            n = T.index(i)
            result += 2**n 

print(convertir([1, 0, 1, 0, 0, 1, 1]))            
