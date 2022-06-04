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


def BFS(graph, node):
    f = [node]
    dist={node:0}
    while len(f)>0:
        node_current = f.pop()
        neighbors = graph.neighbors(node_current)
        for i in neighbors:
            if i not in dist.keys():
                f.insert(0, i)
                dist[i] = dist[node_current] + 1
    return dist

BFS(G1, 'A')
