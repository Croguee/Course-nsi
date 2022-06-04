import matplotlib.pyplot as plt
from compare_tri import compare
from tri_fusion import tri_fusion
from tri_insert import tri_insertion

def compare_graph(f1, f2):
    results = compare(f1, f2)
    plt.figure(figsize=(10, 10))
    x=[r[0] for r in results]
    y1=[r[1]*1000 for r in results]
    y2 =[r[2]*1000 for r in results]
    plt.scatter(x, y1, label='Insert Sort')
    plt.scatter(x, y2, label="Fusion Sort")
    plt.xlabel("Elements in list")
    plt.ylabel("Time (en ms)")
    plt.legend()
    plt.grid(True)
    return plt.show()

print(compare_graph(tri_insertion, tri_fusion)) 


