from analyzer import *
from collections import deque
analizador = Analizer('Laboratorio1/laberinto2.png')
analizador.discretize_image(4)
analizador.crearvecinos()

matriz = (analizador.return_matrix())


init = analizador.inicio
final = analizador.return_goal()





def BFS(destination,start):
    queue = deque([start])
    parents = {start:None}

    while queue:
        node = queue.popleft()
        if node is not None:
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


x = BFS(final[1],init)
lista = []
for nodo in x:
    lista.append(nodo.cellrange)
analizador.pintar_celdas('Laboratorio1/imagen_discretizada.jpg',lista,(0, 0, 255))








