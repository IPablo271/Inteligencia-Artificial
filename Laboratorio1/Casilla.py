
class Casilla():
    def __init__(self,x,y,color,identificador,colori):
        self.posicion = [x,y]
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.color = color
        self.identificador = identificador
        self.colori = colori
    
    def get_posicion(self):
        return [self.posicion[0],self.posicion[1]]
    def get_color(self):
        return(self.color)
    def Movments(self):
        return [self.arriba,self.abajo,self.derecha,self.izquierda]

