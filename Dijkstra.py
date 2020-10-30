
import time
def main():
    #Iniciando menu
    print("Bienvenido al programa ")
    print("-------------------------------")
    print("Seleccione una opcion:\n")
    print("\t1. Ingresar manualmente un grafo")
    print("\t2. Usar los grafos predeterminados para la experimentacion")
    print("\n")
    opcion = input(f'Ingresar numero de la opcion: ')

    if opcion == '1':

        Cantidad_Vertices = int(input(f'Ingresar numero de nodos\n'))
        g = Grafo(Cantidad_Vertices)    
        Cantidad_Aristas = int(input(f'Ingresar numero de aristas\n'))
        for arista in range(Cantidad_Aristas):
            datos= input(f'Ingresar arista {arista}: nodo_origen nodo_destino peso\n')
            datos= datos.split(" ")
            datos=[int(x) for x in datos]
            g.grafo[datos[0]][datos[1]]=datos[2]
        g.Draw()  
        objetivo = int(input(f'Ingresar el nodo para el algoritmo Dijkstra\n'))
        g.Algoritmo_Dijkstra(objetivo);
    elif opcion == '2':
        print("Seleccione el grafo:\n")
        print("\t1. Grafo 5 nodos")
        print("\t2. Grafo 8 nodos")
        print("\t3. Grafo 12 nodos")
        opcion = input(f'Ingresar numero de la opcion: ')
        if opcion == '1':
            pass
        elif opcion == '2':
            pass
        elif opcion == '3':
            pass
class Grafo:
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range (vertices)]

    def Mostrar (self,distancias):
        print(f'Distancias mínimas:\n')
        for nodo in range(self.vertices):
           print(f'{nodo}\t{distancias[nodo]}')

    def DistanciaMinima(self,distancias,SPT):
        distminima = float ('inf')
        for vertice in range(self.vertices):
            if distancias[vertice] < distminima and SPT[vertice] == False:
                distminima = distancias[vertice]
                indice_minimo = vertice

        return indice_minimo

    def Algoritmo_Dijkstra(self,nodo_origen):#partida
        distancias = [float ('inf')] * self.vertices
        distancias [nodo_origen] = 0
        SPT = [False] * self.vertices

        for contador in range(self.vertices):
            nodo_actual = self.DistanciaMinima(distancias,SPT)
            SPT[nodo_actual]=True
            for vertice in range(self.vertices) :
                if self.grafo[nodo_actual][vertice] > 0 and SPT[vertice] == False and distancias[vertice] > distancias[nodo_actual] + self.grafo[nodo_actual][vertice]:
                    distancias[vertice] = distancias[nodo_actual] + self.grafo[nodo_actual][vertice]

        self.Mostrar(distancias)

    def Draw (self):
        grafo = self.grafo
        size = len(self.grafo)
        print('\nGrafo:\n')
        cad = '     '
        for i in range(size):
            cad+=f'|  {i}  '
        print(cad)
        cad='-----'
        for i in range(size):
            cad+=f'|-----'
        print(cad)
        for i in range(size):
            cad = f'  {i}  '
            for j in range(size):
                cad+=f'|  {grafo[i][j]}  '
            print(cad)
        print('\n')
            






        
        
        
        
        





if __name__ =="__main__":
   main()

    