def maxi(tab):
    """
    Function max()
    """
    nb_index = 0
    nb_max = 0
    for i in range(len(tab)):
        if tab[i]>nb_max :
            nb_max,nb_index=tab[i],i
    return nb_max,nb_index


def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

print(positif([-1,0,5,-3,4,-6,10,9,-8 ]))
