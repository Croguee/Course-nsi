
def pascal(n,p,mem = None):
    if mem == None:
        mem = {}
    if p == 0 or n == p:
        return 1
    else:
        if (n,p) in mem.keys():
            return mem[(n,p)]
        else:
            print(mem)
            p1 = pascal(n-1, p-1, mem)
            p2 = pascal(n-1, p, mem)
            mem[(n,p)] = p1 + p2
            return p1 + p2, mem

pascal(5,7)
