
class Casilla():
    def __init__(self,x,y,color,identificador,colori,cellrange):
        self.posicion = [x,y]
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.color = color
        self.identificador = identificador
        self.colori = colori
        self.cellrange = cellrange
        self.mov = []
        
    
    def get_posicion(self):
        return [self.posicion[0],self.posicion[1]]
    
    def get_color(self):
        return(self.color)
    def Movments(self):
        return [self.arriba,self.abajo,self.derecha,self.izquierda]
    def __lt__(self, other):
        return self.posicion[0] < other.posicion[0] and self.posicion[1] < other.posicion[1]

