#
# Exercice 1
#

def recherche(elt, tab):
  """
  renvoie l’indice de la première occurrence de elt
  dans tab si elt est dans tab et -1 sinon
  """
  assert type(elt) == int
  assert type(tab) == list

  if len(tab) == 0:
    return -1

  indice = []

  for i in range(len(tab)):
    if elt == tab[i]:
        indice.append(i)
  
  if len(indice) == 0:
    return -1
  else:
    return indice[0]


assert recherche(1, [2, 3, 4]) == -1
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(50, [1, 50, 1]) == 1
assert recherche(15, [8, 9, 10, 15]) == 3


#
# Exercice 2
#   

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(tab)-1
    while a < l[i] and i >= 0: 
      l[i+1] = l[i]
      l[i] = a
      i = i-1
    return l

assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10,[1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1,[2,3,4]) == [1, 2, 3, 4]