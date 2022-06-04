
def puissanceA(x, n):
    """
    Retourne x à la puissance n
    en utilisant la récursivité basique
    """
    if n==0:
        return 1
    else:
        return x*puissanceA(x, n-1)

#puissanceA(2,6)


def puissanceB(x,n):
    """
    Retourne x à la puissance n
    en utilisant la méthode diviser pour régner    
    """
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2 == 0:
        return puissanceB(x, n/2) ** 2
    else:
        return x * puissanceB(x, n-1)

#puissanceB(2,6)


