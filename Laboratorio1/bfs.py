from Framework import Framework

class BFS(Framework):
    def __init__(self,matriz,estadoinicial,estadofinal):
        super().__init__(matriz,estadoinicial,estadofinal)
    
    def actions(self,nodo):
        nodo.Movemts()
