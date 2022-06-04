from fusion import fusion

def tri_fusion(table):
    # cas d'arrêt : table n'as plus d'élément, donc table est trié
    if len(table)==1:
        return table
    # cas général
    else:
        median = len(table)//2
        sorted_left = tri_fusion(table[:median])
        sorted_right = tri_fusion(table[median:])
        return fusion(sorted_left, sorted_right)

print(tri_fusion([9,8,7,6,5,4,3,2,1,0]))
