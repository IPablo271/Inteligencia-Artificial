from abc import ABC, abstractmethod

class Framework(ABC):
    def __init__(self,destination,start):
        self.destination = destination
        self.start = start
    @abstractmethod
    def actions(self):
        pass
    @abstractmethod
    def result(self):
        pass 
    @abstractmethod
    def goalTest(self,nodo):
        pass
    @abstractmethod
    def step_cost(self):
        pass 
    @abstractmethod
    def path_cost(self):
        pass
    
