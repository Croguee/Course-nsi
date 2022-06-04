#
#   Exercie 1
#

def recherche(tab, n):
    """

    """
    i = 0
    j = len(tab)-1
    while len(tab) > 1:
        mid = (i+j) //2
        if n == tab[mid]:
            return mid
        elif n < tab[mid]:
            j = mid -1
        else:
            i = mid +1
    return -1      
        
print(recherche([1,2,3,4,5,6], 6))

def recursive_recherche(tab, n, mid = -1):
    i = 0
    j = len(tab)-1
    if mid == -1:
        mid = (i1+i2) // 2
    elif n == tab[mid]:
        return mid
    elif n < tab[mid]:
        return recursive_recherche(tab[i, mid], n, mid-1)
    elif n > tab[mid]:
        return recursive_recherche(tab[mid, j], n, mid+1)

print(recursive_recherche([1,2,3,4,5,6], 6)) 