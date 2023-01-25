from analyzer import *
from Nodos import *
analizador = Analizer('Laboratorio1/i.bmp')
analizador.discretize_image(20)
analizador.crearvecinos()
analizador.print_colori()

matriz = (analizador.return_matrix())




