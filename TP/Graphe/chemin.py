import matplotlib.pyplot as plt
import networkx as nx
from parcours_chemin import parcours

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

options = {
    "font_size": 8,
    "node_size": 1000,
    "edgecolors": "#4682B4",
    "alpha": 0.95,
    "linewidths": 2,
    "width": 2,
}


def chemin(G, start, end):
    Previous = parcours(G, start)
    if not Previous or end not in G.nodes:
        return []
    current = end
    path = [current]
    while current != start:
        previous = Previous.get(current)
        if previous:
            path.insert(0, previous)
            current = previous
    return path


path=chemin(G1, "L", "G")
print(path)
plt.figure(figsize=(4,3))

pos = nx.nx_agraph.graphviz_layout(G1)
color_map=['#FFA500' if node in path else '#A0CBE2' for node in G1]
nx.draw(G1, pos, node_color=color_map, with_labels=True, **options)

plt.show()