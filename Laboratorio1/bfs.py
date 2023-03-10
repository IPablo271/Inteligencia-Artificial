from Framework import Framework
from collections import deque


class BFS(Framework):
    def __init__(self,destination,start):
        super().__init__(destination,start)
    
    def actions(self,nodo):
        return nodo.Movments()
    def goalTest(self,nodo):
        if nodo == self.destination:
            return True
        else:
            return False
    def step_cost(self):
        return super().step_cost()
    def path_cost(self):
        return super().path_cost()
    def result(self):
        return super().result()
    def BFSAlgorithm(self):
        queue = deque([self.start])
        parents = {self.start:None}

        while queue:
            node = queue.popleft()
            if node is not None:
                casillaf = self.goalTest(node)
                if casillaf:
                    path = []
                    while node is not None:
                        path.append(node)
                        node = parents[node]
                    return path[::-1]
                vecinos = self.actions(node)
                for vecino in vecinos:
                    if vecino not in parents:
                        queue.append(vecino)
                        parents[vecino] = node

    
    
    



