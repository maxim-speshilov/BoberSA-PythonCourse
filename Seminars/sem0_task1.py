import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

key = ['бумаг', 'камен', 'ножниц', 'ящериц', 'спок']

labels = {
    0: 'бумага',
    1: 'камень',
    2: 'ножницы',
    3: 'ящерица',
    4: 'спок'}

options = {
    'labels': labels,
    'node_color': 'grey',
    'node_size': 1000,
    'line_color': 'grey',
    'width': 1,
}
a = np.zeros((5, 5), dtype=int)

s = 'Это очень просто. Ножницы режут бумагу, бумага накрывает камень, камень давит ящерицу, ящерица травит Спока, Спок ломает ножницы, ножницы отрезают голову ящерице, ящерица ест бумагу, бумага ложится под Спока, Спок испаряет камень, и, как обычно, камень разбивает ножницы.'
for w in [t.split() for t in s.lower().replace('.', ',').split(',')][:-1]:
   if w[-1][:-1] in key:
       if w[0] == 'спок':
           #print(key.index(w[0]), w[0], ' - ', w[-1], key.index(w[-1][:-1]))
           a[key.index(w[0])][key.index(w[-1][:-1])] = 1
       else:
           #print(key.index(w[0][:-1]), w[0], ' - ', w[-1], key.index(w[-1][:-1]))
           a[key.index(w[0][:-1])][key.index(w[-1][:-1])] = 1

D = nx.DiGraph(a)
fig = nx.draw_circular(D, **options)
fig.canvas.set_window_title('Test')
plt.show()
