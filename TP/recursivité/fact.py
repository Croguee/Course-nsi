def rfact(n):
    if n<=0: # situation d'arrêt
        return 1
    else:
        return n*rfact(n-1) #appel récursif, la variable n décroit
    
rfact(4)