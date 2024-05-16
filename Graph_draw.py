import networkx as nx
import matplotlib as plt

G = nx.Graph()

nodes = ['Київ', 'Львів', 'Одеса', 'Харків', 'Дніпро']

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

G.add_nodes_from(nodes)

nx.draw_graph(G, node_size=500, node_color='skyblue', edge_color='black', width=1.5)
plt.show()




