#
# Exercice 1
#

def occurence_lettres(phrase):
    assert type(phrase) == str
    dico = {}
    for i in phrase:
        if i in dico.keys():
            dico[i] += 1
        else:
            dico[i] = 1
    return dico


#
# Exercice 2
#

def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
        L12[i] = L1[i1]
        i1 = i1 + 1
        i += 1 
    while i2 < n2:
        L12[i] = L2[i2]
        i2 = i2 + 1
        i += 1 
    return L12

print(fusion([1,6,10],[0,7,8,9]))
        
