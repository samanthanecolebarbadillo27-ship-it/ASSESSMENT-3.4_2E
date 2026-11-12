
from collections import deque

graph = {}


def add_edge(a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    order = []
    visited = [start]
    queue = deque()
    queue.append(start)

    while len(queue) > 0:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return order


def dfs(current, visited, order):
    visited.append(current)
    order.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(neighbor, visited, order)


add_edge("B1", "A1")
add_edge("B1", "R")
add_edge("A1", "A2")
add_edge("R", "B2")
add_edge("A2", "B2")
add_edge("A2", "D")
add_edge("B2", "I")
add_edge("D", "L1")
add_edge("I", "L2")
add_edge("I", "O")
add_edge("L1", "L2")

for vertex in graph:
    graph[vertex].sort()

print("=== GRAPH ===")
for vertex in graph:
    print(vertex + ": " + ", ".join(graph[vertex]))

bfs_order = bfs("B1")

dfs_order = []
dfs("B1", [], dfs_order)

print("BFS: " + " -> ".join(bfs_order))
print("DFS: " + " -> ".join(dfs_order))