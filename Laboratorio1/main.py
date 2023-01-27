from analyzer import *
from collections import deque
import heapq
analizador = Analizer('Laboratorio1/i.bmp')
analizador.discretize_image(25)
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
def DFS(destination, start):
    stack = [start]
    parents = {start: None}

    while stack:
        node = stack.pop()
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
                    stack.append(vecino)
                    parents[vecino] = node

    return None

import heapq

def A_star(destination, start):
    heap = [(heuristic_distance(start, destination), start)]  # Use a heap to store the nodes to visit
    parents = {start: None}
    g_score = {start: 0}  # g_score is the distance from the start node

    while heap:
        current = heapq.heappop(heap)[1]  # Get the node with the lowest f_score
        if current is not None:
            if current == destination:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                return path[::-1]

            neighbors = current.Movments()
            for neighbor in neighbors:
                if neighbor is not None:
                    tentative_g_score = g_score[current] + distance(current, neighbor)
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        parents[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score = g_score[neighbor] + heuristic_distance(neighbor, destination)
                        heapq.heappush(heap, (f_score, neighbor))

    return None

def heuristic_distance(current, destination):
    if current and destination is not None:
        return abs(current.posicion[0] - destination.posicion[0]) + abs(current.posicion[1] - destination.posicion[1])


def distance(current, neighbor):
    if current and neighbor is not None:
        return ((current.posicion[0] - neighbor.posicion[0])**2 + (current.posicion[1] - neighbor.posicion[1])**2)**0.5

x = A_star(final[1],init)

lista = []
for nodo in x:
    lista.append(nodo.cellrange)
analizador.pintar_celdas('Laboratorio1/imagen_discretizada.jpg',lista,(0, 0, 255))








