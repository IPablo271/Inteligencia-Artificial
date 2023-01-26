from analyzer import *
from collections import deque
analizador = Analizer('Laboratorio1/i.bmp')
analizador.discretize_image(25)
analizador.crearvecinos()

matriz = (analizador.return_matrix())


init = analizador.inicio
final = analizador.return_goal()




print(init)
print(final)


def BFS(destination,start):
    queue = deque([start])
    parents = {start:None}

    while queue:
        node = queue.popleft()
        if node == destination:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            return path[::-1]
        vecinos = node.Movments()
        for vecino in vecinos:
            if vecino not in parents:
                queue.append(vecino)
                parents[vecino] = node

        
    return None

BFS(final[0],init)








