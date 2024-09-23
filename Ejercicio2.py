"""
2.	Crea dos arreglos unidimensionales que tengan el mismo tamaño (lo pedirás por teclado). En uno de ellos 
almacenarás nombres de productos como cadenas, y en el otro arreglo almacenarás los precios de esos productos
(como números de punto flotante). Muestra por pantalla el nombre del producto y su precio, que estén contenidos
en un tercer arreglo. Puedes usar funciones.
"""

def creararreglo(tamaño):
    productos = []
    precios = []
    for i in range(tamaño):
        producto = input(f"Dame el nombre del producto {i+1}:")
        precio = float(input(f"Dame el precio del producto {i+1}:"))
        productos.append(producto)
        precios.append(precio)
    return productos, precios

def tercerarreglo(productos, precios):
    arreglo3 = []
    for i in range(len(productos)):
        arreglo3.append(f"Nombre: {productos[i]} --- Precio: {precios[i]}")
    return arreglo3

def main():
    tamaño = int(input("Dame el numero de tamaño que quieres tu arreglo:"))
    productos,precios = creararreglo(tamaño)
    arreglo3 = tercerarreglo(productos, precios)   
    for i in range(len(arreglo3)):
        print(f"{i+1}: {arreglo3[i]}")

main()






