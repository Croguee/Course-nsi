#
# Exercice 1
#

def mini(releve, date):
    """
    renvoie la plus petite valeur relevée au cours de la
    période et l’année correspondante.
    """
    assert isinstance(releve, list)
    assert isinstance(date, list)

    minimun = 0
    annee = 0
    for i in range(1, len(releve)):
        if releve[i] < releve[i-1]:
            minimun = releve[i]
            annee = date[i]
    return minimun, annee
            
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert mini(t_moy, annees) == (12.5, 2016)

#
# Exercice 2
#

def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result
    return result   

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)


assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True