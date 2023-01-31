from analyzer import *
from bfs import *
from dfs import *
from Astar import *


analizador = Analizer('Laboratorio1/i.bmp')
analizador.discretize_image(25)
analizador.crearvecinos()




init = analizador.inicio
final = analizador.return_goal()



salir = False
while salir == False:
    print("1. Analizar con algoritmo BFS")
    print("2. Analizar con algoritmo DFS")
    print("3. Analizar con algoritmo A*")
    print("4. Salir del programa")
    var = input("Seleccione una opcion: ")

    if var =="1":
        Bfsinstance = BFS(final[1],init)
        result = Bfsinstance.BFSAlgorithm()
        lista = []
        for nodo in result:
            lista.append(nodo.cellrange)
        analizador.pintar_celdas('Laboratorio1/imagen_discretizada.jpg',lista,(0, 0, 255))
    elif var == "2":
        DFSfsinstance = DFS(final[1],init)
        result = DFSfsinstance.DFSalgoritmo()
        lista = []
        for nodo in result:
            lista.append(nodo.cellrange)
        analizador.pintar_celdas('Laboratorio1/imagen_discretizada.jpg',lista,(0, 0, 255))
    elif var == "3":
        Astarinstance = Astar(final[1],init)
        result = Astarinstance.A_star()
        lista = []
        for nodo in result:
            lista.append(nodo.cellrange)
        analizador.pintar_celdas('Laboratorio1/imagen_discretizada.jpg',lista,(0, 0, 255))
    
    elif var == "4":
        salir = True
        print("Saliendo del programa")






# Bfsinstance = BFS(final[1],init)
#DFSfsinstance = DFS(final[1],init)
Astarinstance = Astar(final[1],init)



result = Astarinstance.A_star()





















