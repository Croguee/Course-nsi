

def pgcd(a, b):
    if a < b:           # si b est supérieu à a
        a,b = b,a
    if a >= b:
        reste = a%b
        if reste == 0:  # cas d'arrêt
            return b
        else:           # cas général
            return pgcd(b, reste)

#print(pgcd(4950,1540))


def puissance(a, b):
    if b == 0:
        return 1
    else:
        return a*(puissance(a, b-1))

#print(puissance(2,10))


def isPalindrome(mot):
    if len(mot) <= 1:
        return True
    elif mot[0] == mot[-1]:
        return isPalindrome(mot[1:-1])
    else:
        return False
        
#print(isPalindrome('kayak'))

def fib(n, mem = None): # Ne jamais passer un type mutable en paramètre par défaut [], {}...
    if mem == None:
        mem={0:0, 1:1} #On mémorise les 2 premieres valeurs
    """
    Si la clé n'existe pas, on affecte le résultat de l'appel récursif dans la mémoire
    Dans tous les cas, on retourne le résultat présent dans la mémoire
    """
    if n < 2:
        return n
    elif n in mem.keys():
        return mem[n]
    else:
        return(mem[n] = fib(n-1)+fib(n-2))

print(fib(1000))        

























