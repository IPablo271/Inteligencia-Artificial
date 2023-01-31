
from Framework import Framework
import heapq

class Astar(Framework):
    def __init__(self,destination,start):
        super().__init__(destination,start)
    
    def actions(self,nodo):
        return nodo.Movments()
    def goalTest(self,nodo):
        if nodo == self.destination:
            return True
        else:
            return False
    def step_cost(self,current,destination):
        if current and destination is not None:
            return abs(current.posicion[0] - destination.posicion[0]) + abs(current.posicion[1] - destination.posicion[1])
    def path_cost(self,current,neighbor):
        if current and neighbor is not None:
            return ((current.posicion[0] - neighbor.posicion[0])**2 + (current.posicion[1] - neighbor.posicion[1])**2)**0.5
    def result(self):
        return super().result()

    def A_star(self):
        heap = [(self.step_cost(self.start, self.destination), self.start)]  # Use a heap to store the nodes to visit
        parents = {self.start: None}
        g_score = {self.start: 0}  # g_score is the distance from the start node

        while heap:
            current = heapq.heappop(heap)[1]  # Get the node with the lowest f_score
            if current is not None:
                casillaf = self.goalTest(current)
                if casillaf:
                    path = []
                    while current is not None:
                        path.append(current)
                        current = parents[current]
                    return path[::-1]
                
                neighbors = self.actions(current)
                for neighbor in neighbors:
                    if neighbor is not None:
                        tentative_g_score = g_score[current] + self.path_cost(current, neighbor)
                        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                            parents[neighbor] = current
                            g_score[neighbor] = tentative_g_score
                            f_score = g_score[neighbor] + self.step_cost(neighbor, self.destination)
                            heapq.heappush(heap, (f_score, neighbor))

        return None



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