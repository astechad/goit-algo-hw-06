import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створення графа для моделювання топології Інтернету
# Граф зі 100 вершинами, побудований за моделлю Барбаші-Альберт
G = nx.scale_free_graph(100)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # Розташування вершин
nx.draw(G, pos, node_size=50, node_color="skyblue",
        edge_color="gray", with_labels=False)
plt.title("Топологія Інтернету (Scale-Free Graph)", fontsize=14)
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [deg for _, deg in G.degree()]

{
    "Кількість вершин": num_nodes,
    "Кількість ребер": num_edges,
    "Середній ступінь вершини": sum(degrees) / len(degrees),
    "Максимальний ступінь вершини": max(degrees),
    "Мінімальний ступінь вершини": min(degrees),
}


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))
    return None


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))
    return None


# Вибір початкової та кінцевої вершин (можете змінити)
start_node = 0
goal_node = 99

# Пошук шляху за допомогою DFS
dfs_path = dfs(G, start_node, goal_node)

# Пошук шляху за допомогою BFS
bfs_path = bfs(G, start_node, goal_node)

# Виведення результатів
print("Шлях за алгоритмом DFS:", dfs_path)
print("Шлях за алгоритмом BFS:", bfs_path)

# Порівняння та аналіз (ви можете додати тут більш детальний аналіз)
if dfs_path and bfs_path:
    print("Обидва алгоритми знайшли шлях.")
    # Порівняння довжини шляхів, кількості відвіданих вершин тощо
else:
    print("Шлях не знайдено.")
