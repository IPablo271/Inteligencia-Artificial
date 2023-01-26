from abc import ABC, abstractmethod

class Framework(ABC):
    def __init__(self,matriz):
        self.estadoInicial = None
        self.goal = []
        self.matriz = matriz
    @abstractmethod
    def actions(self):
        pass
    @abstractmethod
    def result(self):
        pass 
    @abstractmethod
    def goalTest(self):
        pass
    @abstractmethod
    def step_cost(self):
        pass 
    @abstractmethod
    def path_cost(self):
        pass
    
