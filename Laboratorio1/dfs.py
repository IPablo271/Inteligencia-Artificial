from Framework import Framework
from collections import deque


class DFS(Framework):
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
    def DFSalgoritmo(self):
        stack = [self.start]
        parents = {self.start: None}

        while stack:
            node = stack.pop()
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
                        stack.append(vecino)
                        parents[vecino] = node

        return None

    
    
    



