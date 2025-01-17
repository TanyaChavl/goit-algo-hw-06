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

plt.show()

# Розрахунок базових метрик для графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
density = nx.density(G) 
avg_degree = sum(dict(G.degree()).values()) / float(num_nodes)

(num_nodes, num_edges, density, avg_degree)

#Характеристики графа:

# Кількість вузлів (станцій/зупинок): 10
# Кількість ребер (маршрутів): 12
# Щільність мережі: Приблизно 0.133, що є співвідношенням фактичних ребер до максимально можливої кількості ребер у спрямованому графі.
# Середній ступінь: 2.4, що є середньою кількістю ребер на вузол.

# Графічне представлення показує просту мережу, де кожен вузол з'єднаний принаймні з одним іншим, 
# а деякі вузли служать вузлами з кількома з'єднаннями. Щільність мережі низька, що вказує на те, що мережа 
# не дуже щільно з'єднана; це типово для транспортних мереж, де не кожна зупинка безпосередньо з'єднана з кожною 
# іншою зупинкою. Середній ступінь каже, що в середньому кожна станція або зупинка з'єднана приблизно 
# з 2-3 іншими станціями або зупинками.
