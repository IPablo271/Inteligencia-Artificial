from PIL import Image,  ImageDraw
from collections import Counter
from Casilla import Casilla


class Analizer():
    def __init__(self, path):
        self.path = path
        self.width = None
        self.height = None
        self.pixels = []
        self.red = False
        self.goal = []
        self.inicio = None
        self.size = 0
    def discretize_image(self,size):
        # Cargar imagen
        im = Image.open(self.path)
        # Obtener las dimensiones de la imagen
        self.width, self.height = im.size
        # Crear una imagen vacía para guardar el color mas recurrente de cada celda
        im_result = Image.new(im.mode, (self.width,self.height))
        # Crear un objeto para dibujar en la imagen
        draw = ImageDraw.Draw(im_result)
        #Recorrer el grid
        ide = 0
        for i in range(0, self.width, size):
            # Lista de filas para almacenar los datos
            fila = []
            for j in range(0, self.height, size):
                #Rango de pixeles
                cell_range = (j,i, j+size, i+size)
                #Obtener el bloque de datos a analizar
                cell = im.crop(cell_range)
                #Color mas frecuente en el bloque de datos
                color, count = Counter(cell.getdata()).most_common(1)[0]
                 
                #Pintar la celda del color que mas se repita en esa celda
                im_result.paste(color, cell_range)
                # Dibujar un borde negro alrededor de la celda actual
                #draw.rectangle([i, j, i+size, j+size], outline=(0, 0, 0))
                # Agregar el color de la celda a la lista de colores

                if color == (254, 0, 0) or color == (237, 28, 36, 255):
                    colori = 3
                    casillatemp = Casilla(i,j,color,ide,colori)
                    self.inicio = casillatemp
                    fila.append(casillatemp)
                if color == (0 , 255, 1) or color == (34, 177, 76, 255):
                    colori = 2
                    casillatemp = Casilla(i,j,color,ide,colori)
                    self.goal.append(casillatemp)
                    fila.append(casillatemp)
                if color == (255 , 255, 255):
                    colori = 1
                    casillatemp = Casilla(i,j,color,ide,colori)
                    fila.append(casillatemp)
                else:
                    colori= 0
                    casillatemp = Casilla(i,j,color,ide,colori)
                    fila.append(casillatemp)
    
                
                ide += 1

            # Se agrega la fila a la lista de bloques
            self.pixels.append(fila)
        
        im_result = im_result.convert("RGB")
        im_result.save("imagen_discretizada.jpg")
        self.sizematriz()

        #Se guarda la imagen 
    def sizematriz(self):
        self.size = int(len(self.pixels))
    def crearvecinos(self):
        for x in range(self.size):
            for y in range(self.size):
                nodocolor = self.pixels[x][y]
                if nodocolor.color == (0, 0, 0):
                    pass 
                else:
                    if x != 0:
                        nodo = self.pixels[x][y]
                        nodoarriba = self.pixels[x-1][y]
                        if nodoarriba.color == (0, 0, 0):
                            pass
                        else:
                            nodo.arriba = self.pixels[x-1][y]

                    if y != 0:
                        nodo = self.pixels[x][y]
                        nodoizquierda = self.pixels[x][y-1]
                        if nodoizquierda.color == (0, 0, 0):
                            pass
                        else:
                            nodo.izquierda = self.pixels[x][y-1] 
                       
                    try:
                        if self.pixels[x+1][y]:
                            nodo = self.pixels[x][y]
                            nodoabajo = self.pixels[x+1][y]
                            if nodoabajo.color == (0, 0, 0):
                                pass
                            else:
                                nodo.abajo = self.pixels[x+1][y]
                    
                    except:
                        pass
                    try:
                        if self.pixels[x][y+1]:
                            nodo = self.pixels[x][y]
                            nododrecha = self.pixels[x][y+1]
                            if nododrecha.color == (0, 0, 0):
                                pass
                            else:
                                nodo.derecha = self.pixels[x][y+1]

                    except:
                        pass
                               
    def load_listamov(self):
        for x in range(self.size):
            for y in range(self.size):
                nodo = self.pixels[x][y]

          
                    
    def print_colori(self):
        for x in range(self.size):
            for y in range(self.size):
                nodo = self.pixels[x][y]
                print(nodo.colori)
    
    def print_movimientos(self):
        for x in range(self.size):
            for y in range(self.size):
                nodo = self.pixels[x][y]
                print("Nodo: "+str(nodo.identificador))
                print(nodo.Movments())



    def print_colors(self):
        for x in range(5):
            for y in range(5):
                print(self.pixels[x][y].color)        

    def print_pixels(self): # Metodo para imprimir el color de los pixeles en el bloque
        print(self.pixels)
    def return_matrix(self):
        return (self.pixels)
    def print_inicio(self):
        print(self.inicio)
    def print_final(self):
        print(self.goal)
    def return_goal(self):
        return (self.goal)

    
