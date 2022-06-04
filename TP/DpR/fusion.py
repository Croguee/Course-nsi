def fusion(T1, T2):
    """
    T1 : une liste triée
    T2 : une liste triée
    Retourne la fusion des 2 listes triée
    """
    result=[]
    i1 = i2 = 0
    while not (i1>=len(T1) or i2>=len(T2)): #on arête si un des deux arrive à la fin
        if T1[i1]>T2[i2]:
            result.append(T2[i2])
            i2+=1
        else:
            result.append(T1[i1])
            i1+=1
    #fin du while
    result.extend(T1[i1:]) # un des deux est une liste vide
    result.extend(T2[i2:])
    return result


# print(fusion([1,3,4,7], [2,5,6,9]))
