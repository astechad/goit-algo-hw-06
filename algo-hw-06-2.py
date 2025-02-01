import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створення графа за моделлю Барбаші-Альберт
G = nx.scale_free_graph(100)

# Візуалізація графа
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_size=50, node_color="skyblue",
        edge_color="gray", with_labels=False)
plt.title("Топологія Інтернету (Scale-Free Graph)", fontsize=14)
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = [deg for _, deg in G.degree()]

print({
    "Кількість вершин": num_nodes,
    "Кількість ребер": num_edges,
    "Середній ступінь вершини": sum(degrees) / len(degrees),
    "Максимальний ступінь вершини": max(degrees),
    "Мінімальний ступінь вершини": min(degrees),
})


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path
            for neighbor in graph.neighbors(vertex):
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
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))
    return None


# Вибір початкової та кінцевої вершин
start_node = 0
goal_node = 99

# Перевірка, чи існує шлях між вершинами
if nx.has_path(G, start_node, goal_node):
    # Пошук шляху за допомогою DFS
    dfs_path = dfs(G, start_node, goal_node)
    # Пошук шляху за допомогою BFS
    bfs_path = bfs(G, start_node, goal_node)

    # Виведення результатів
    print("Шлях за алгоритмом DFS:", dfs_path)
    print("Шлях за алгоритмом BFS:", bfs_path)

    # Порівняння результатів
    if dfs_path and bfs_path:
        print("Обидва алгоритми знайшли шлях.")
        print("Довжина шляху DFS:", len(dfs_path))
        print("Довжина шляху BFS:", len(bfs_path))

        if len(dfs_path) > len(bfs_path):
            print("BFS знайшов коротший шлях, оскільки обходить граф рівномірно.")
        else:
            print("DFS міг знайти коротший або довший шлях залежно від порядку обходу.")
    else:
        print("Один з алгоритмів не знайшов шлях.")
else:
    print("Шлях між обраними вершинами не існує.")

# Запис висновків у файл readme.md
with open("readme.md", "w", encoding="utf-8") as f:
    f.write("# Порівняння алгоритмів DFS та BFS у графі\n")
    f.write("Ця програма використовує алгоритми DFS та BFS для пошуку шляхів у графі, "
            "створеному за моделлю Барбаші-Альберт.\n\n")
    f.write("## Висновки\n")
    f.write("- BFS зазвичай знаходить найкоротший шлях у ненаправлених графах.\n")
    f.write("- DFS може знайти довший або коротший шлях залежно від порядку обходу.\n")
    f.write("- Якщо граф містить шлях між вершинами, обидва алгоритми його знайдуть.\n")
