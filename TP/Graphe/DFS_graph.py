import matplotlib.pyplot as plt
import networkx as nx

# Instantiation d'un graphe
G1 = nx.Graph()
edges = [('A', 'B'),
         ('A', 'C'),
         ('A', 'D'),
         ('B', 'E'),
         ('C', 'F'),
         ('C', 'I'),
         ('D', 'G'),
         ('B', 'H'),
         ('H', 'I'),
         ('F', 'J'),
         ('E', 'K'),
         ('K', 'G'),
         ('J', 'L'),
        ]
# Ajout des arêtes pondérés
for edge in edges:
    G1.add_edge(edge[0], edge[1])

def DFS_rec(g, node, visits_nodes=None):
    if visits_nodes == None:
        visits_nodes = []
    if node not in visits_nodes:
        visits_nodes.append(node)
        for i in g.neighbors(node):
            DFS_rec(g, i, visits_nodes)
    return visits_nodes

visits_nodes = DFS_rec(G1, "A")
print(visits_nodes)