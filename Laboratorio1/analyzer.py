from PIL import Image,  ImageDraw
from collections import Counter


class Analizer():
    def __init__(self, path):
        self.path = path
        self.width = None
        self.height = None
        self.pixels = []
        self.pixels_copy = []
        self.size_pixels = None
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
                fila.append(color)
            # Se agrega la fila a la lista de bloques
            self.pixels.append(fila)
        im_result = im_result.convert("RGB")
        im_result.save("imagen_discretizada.jpg")
        #Se guarda la imagen generada

    def print_pixels(self): # Metodo para imprimir el color de los pixeles en el bloque
        print(self.pixels)

    
