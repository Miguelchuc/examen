def calcular_agua_por_organismo(agua_inicial, generaciones):
    if generaciones < 0 or generaciones > 50:
        raise ValueError("El número de generaciones debe estar entre 0 y 50.")
    
   
    agua_por_organismo = agua_inicial / (2 ** generaciones)
    
    return agua_por_organismo


try:
    agua_inicial = float(input("Ingrese la cantidad inicial de agua (en litros): "))
    generaciones = int(input("Ingrese el número de generaciones (0 a 50): "))

    if agua_inicial <= 0:
        print("Error: La cantidad inicial de agua debe ser mayor que 0.")
    elif generaciones < 0 or generaciones > 50:
        print("Error: El número de generaciones debe estar entre 0 y 50.")
    else:
    
        agua_por_organismo = calcular_agua_por_organismo(agua_inicial, generaciones)
        print(f"Cantidad de agua por organismo después de {generaciones} generaciones: {agua_por_organismo:.10f} litros")
except ValueError as e:
    print(f"Error: {e}")
