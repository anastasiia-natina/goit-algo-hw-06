import networkx as nx
import matplotlib as plt
from networkx.algorithms.traversal import dfs_tree, bfs_tree
from networkx.algorithms.shortest_paths import dijkstra_shortest_path

G = nx.Graph()

G.add_nodes(['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро'])

G.add_edges_from([
    ('Київ', 'Львів', 540),
    ('Київ', 'Одеса', 480),
    ('Київ', 'Харків', 490),
    ('Київ', 'Дніпро', 496),
    ('Львів', 'Одеса', 1000),
    ('Львів', 'Харків', 750),
    ('Львів', 'Дніпро', 810),
    ('Одеса', 'Харків', 700),
    ('Одеса', 'Дніпро', 630),
    ('Харків', 'Дніпро', 240)
], weight=True)

nx.draw_graph(G, node_size=500, node_color='skyblue', edge_color='black', width=1.5)
plt.show()

print("Кількість вершин:", G.number_of_nodes())  
print("Кількість ребер:", G.number_of_edges())  
print("Ступінь вершин:")
for node in G.nodes():
    degree = G.degree[node]
    print(f" - {node}: {degree}")

dfs_path = list(dfs_tree(G, 'Київ', 'Дніпро'))
print("Шлях DFS від Києва до Дніпра:", dfs_path)

bfs_path = list(bfs_tree(G, 'Київ', 'Дніпро'))
print("Шлях BFS від Києва до Дніпра:", bfs_path)

for destination in G.nodes():
    if destination != 'Київ':
        path = dijkstra_shortest_path(G, 'Київ', destination)
        weight = nx.shortest_path_length(G, 'Київ', destination)
        print(f"Найкоротший шлях від Києва до {destination}:", path, f"({weight} км)")

nx.draw_shortest_path(G, 'Київ', 'Львів', edge_color='red', width=2)
plt.show()