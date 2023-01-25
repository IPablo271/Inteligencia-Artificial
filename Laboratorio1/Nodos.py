from Casilla import *

class Nodos():
    def __init__(self, matriz):
        self.matriz = matriz
        self.goal = None
        self.start = None
        self.height = len(self.matriz)
        self.width = len(self.matriz)
        self.MatrizNodo = [[0 for x in range(0,self.width)]
                            for y in range(0,self.height)]

   

    def returnMatrizNodos(self):
        print(self.MatrizNodo)


