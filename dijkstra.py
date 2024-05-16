import heapq
from Graph_draw import *

def dijkstra_distance(graph, start):

    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    previous = {node: None for node in graph.nodes()}

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges(current_node, data=True):
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, previous


start_node = 'Київ'
distances, previous = dijkstra_distance(G, start_node)

for end_node in G.nodes():
    path = []
    current_node = end_node
    while current_node != start_node:
        path.append(current_node)
        current_node = previous[current_node]
    path.reverse()
    print(f"Найкоротший шлях з {start_node} до {end_node}:", ' -> '.join(path))