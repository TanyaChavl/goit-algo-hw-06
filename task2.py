from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

# Граф транспортної мережі

G = nx.DiGraph()

# Додаю вузли (станції/зупинки) на графік
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

# Додаю ребра (маршрути) між вузлами
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('C', 'E')
G.add_edge('D', 'F')
G.add_edge('E', 'G')
G.add_edge('F', 'H')
G.add_edge('G', 'H')
G.add_edge('H', 'I')
G.add_edge('I', 'J')
G.add_edge('J', 'A')

# Малюю граф
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)

# Відключила відображення графа. В даний момент воно не потрібно.
#plt.show()

# Розрахунок базових метрик для графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
density = nx.density(G) 
avg_degree = sum(dict(G.degree()).values()) / float(num_nodes)

(num_nodes, num_edges, density, avg_degree)

# Реалізація DFS алгоритма
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.successors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

# реалізація BFS алгоритма
def bfs(graph, start, goal):
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        (vertex, path) = queue.get()
        for next in set(graph.successors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.put((next, path + [next]))

# Використовую DFS і BFS для пошуку шляху від A до I
dfs_path = dfs(G, 'A', 'I')
bfs_path = bfs(G, 'A', 'I')

print(f"Шлях за алгоритмом DFS: {(dfs_path)}")
print(f"Шлях за алгоритмом BFS: {(bfs_path)}")

# Пояснення різниці в шляхах
# DFS (Пошук в глибину): Алгоритм намагається "зануритися" якомога глибше в граф, перш ніж повертатися до інших 
# сусідів вихідної вершини. У цьому випадку, він переходить від точки A до B, потім до D, і так далі, доки не досягне I, 
# формуючи шлях через вершини на "одній з гілок" графа.

# BFS (Пошук в ширину): Алгоритм розглядає всі сусідні вершини, перш ніж переходити на наступний рівень глибини. 
# Таким чином, він вибудовує шлях від A до I, послідовно проходячи через вершини, які знаходяться ближче за 
# рівнями віддаленості від початкової точки.

#Чому шляхи саме такі?
# Вплив алгоритму на вибір шляху: DFS може знайти шлях швидше в глибоких і складних графах, де шуканий елемент 
# знаходиться далеко від початкової точки, але цей шлях не завжди буде найкоротшим. BFS, навпаки, завжди знаходить 
# найкоротший шлях у графах без ваг ребер, як це і є в нашому випадку, хоча це може вимагати більше часу та пам'яті для великих графів.
# Специфіка графа: В даному графі обидва алгоритми знайшли різні шляхи через специфіку з'єднань між вершинами. 
# DFS швидше "занурився" у глиб графа, проходячи через вершини B, D, F, досягаючи I. BFS послідовно розширював пошук від 
# A до сусідів і далі по рівнях, знаючи найкоротший шлях через C, E, G до I.
# Таким чином, вибір між DFS та BFS залежить від конкретних задач та структури графа.