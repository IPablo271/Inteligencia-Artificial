from abc import ABC, abstractmethod

class Framework(ABC):
    @abstractmethod
    def actions(self, state):
        return
    @abstractmethod
    def result(self, state, action):
        return  
    @abstractmethod
    def goalTest(self, state):
        return
    @abstractmethod
    def step_cost(self, state):
        return 
    @abstractmethod
    def path_cost(self, state):
        return 
    
