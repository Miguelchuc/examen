import random
import time

class BusquedaNumeros:
    def _init_(self):
        self.numeros = []

    def Generar_Numeros(self, cantidad=500):
        self.numeros = [random.randint(0, 1000) for _ in range(cantidad)]
        print("Lista generada: ")
        print(self.numeros)

    def Solicitar_Numero(self):
        self.numero_buscado = int(input("Ingrese el número que desea buscar: "))
        
    def Busqueda_Lineal(self):
        print("\n Búsqueda lineal")
        inicio = time.time()
        for i in range(len(self.numeros)):
            if self.numeros[i] == self.numero_buscado:
                fin = time.time()
                print(f"Número {self.numero_buscado} encontrado en la posición {i} mediante búsqueda lineal.")
                print(f"Tiempo de ejecución de búsqueda lineal: {fin - inicio} segundos.")
                return i
        fin = time.time()
        print(f"Número {self.numero_buscado} no encontrado mediante búsqueda lineal.")
        print(f"Tiempo de ejecución de búsqueda lineal: {fin - inicio} segundos.")
        return -1

    def Busqueda_Binaria(self):
        print("\n Búsqueda binaria")
        self.numeros.sort() 
        inicio = time.time()
        inicio_lista, fin_lista = 0, len(self.numeros) - 1

        while inicio_lista <= fin_lista:
            mitad = (inicio_lista + fin_lista) // 2
            if self.numeros[mitad] == self.numero_buscado:
                fin = time.time()
                print(f"Número {self.numero_buscado} encontrado en la posición {mitad} mediante búsqueda binaria.")
                print(f"Tiempo de ejecución de búsqueda binaria: {fin - inicio} segundos.")
                return mitad
            elif self.numeros[mitad] < self.numero_buscado:
                inicio_lista = mitad + 1
            else:
                fin_lista = mitad - 1

        fin = time.time()
        print(f"Número {self.numero_buscado} no encontrado mediante búsqueda binaria.")
        print(f"Tiempo de ejecución de búsqueda binaria: {fin - inicio} segundos.")
        return -1


programa = BusquedaNumeros()
programa.Generar_Numeros()  
programa.Solicitar_Numero()  
programa.Busqueda_Lineal()  
programa.Busqueda_Binaria()