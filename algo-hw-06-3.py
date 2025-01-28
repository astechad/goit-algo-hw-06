# ... ваш попередній код

# Знаходження найкоротшого шляху між двома конкретними вершинами
def shortest_path(from_node, to_node):
    path = []  # Ініціалізуємо список для шляху
    node = to_node
    while node != from_node:
        path.append(node)
        node = paths[node]
    path.append(from_node)
    return path[::-1]

# ... решта вашого коду
