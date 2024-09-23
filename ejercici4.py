
arreglo_a = ["MARIANA", "JOSE", "EDUARDO", "FEDE", "ARTURO", "JULIAN", "PANCHO", "MIRIAN", "PEPE"]
arreglo_b = ["ADRIANA", "ALEX", "OSI", "PABLO", "JUAN", "PAULA", "MIKE", "EFRA", "PACO"]

def agregar_estu(arreglo, nombre_arreglo):
    estudiante = input(f"Ingresa el nombre del estudiante para {nombre_arreglo}: ")
    arreglo.append(estudiante)
    imprimir_arreglo(arreglo, nombre_arreglo)  

def mostrar_unicos(arregloa, arreglob, nombre):
    print(f"Estudiantes únicos en {nombre}:")
    for estudiante in arregloa:
        if estudiante not in arreglob:
            print(estudiante)

def mostrar_comunes(arregloa, arreglob):
    print("Estudiantes comunes:")
    for estudiante in arregloa:
        if estudiante in arreglob:
            print(estudiante)

def imprimir_arreglo(arreglo, nombre):
    print(f"Estudiantes en {nombre}: {arreglo}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Agregar estudiante al arreglo A")
        print("2. Agregar estudiante al arreglo B")
        print("3. Mostrar estudiantes únicos en A")
        print("4. Mostrar estudiantes únicos en B")
        print("5. Mostrar estudiantes comunes")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_estu(arreglo_a, "A")
        elif opcion == "2":
            agregar_estu(arreglo_b, "B")
        elif opcion == "3":
            mostrar_unicos(arreglo_a, arreglo_b, "A")
        elif opcion == "4":
            mostrar_unicos(arreglo_b, arreglo_a, "B")
        elif opcion == "5":
            mostrar_comunes(arreglo_a, arreglo_b)
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    imprimir_arreglo(arreglo_a, "A")  
    imprimir_arreglo(arreglo_b, "B") 
    menu()
