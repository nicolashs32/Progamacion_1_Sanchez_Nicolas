

def mostrar_atracciones ():
    print("Menu de atracciones")
    print("1_Montaña rusa")
    print("2_Carrusel")
    print("3_casa del terror")
    selecion_atracciones = int(input(f"enumere cuantas atracciones desea visitar: "))
    atracciones = ""
    for i in range(selecion_atracciones):

        atraccion = int(input(f"selecciones atraccion a visitar {i+1}: ")) 
        atracciones += atraccion
    return atracciones

def puede_subir(edad, atraccion):
    if atraccion == "Montaña Rusa" and edad < 12:
        return False
    elif edad < 6 and atraccion != "Carrusel":
        return False
    return True

def calcular_precio(atraccion):
    return atracciones[atraccion]

def registrar_visita():
    nombre = input("Ingrese el nombre del visitante: ")
    edad = int(input("Ingrese la edad del visitante: "))
    cant_atracciones = int(input("¿Cuántas atracciones desea usar? (máx 3): "))

    elegidas = ""
    usadas = ""
    costo_total = 0

    mostrar_atracciones()

    for i in range(cant_atracciones):
        opcion = int(input(f"Seleccione la atracción {i+1} (1-3): "))
        atraccion = list(atracciones.keys())[opcion - 1]
        elegidas.append(atraccion)

        if puede_subir(edad, atraccion):
            print(f"Puede subir a la {atraccion}.")
            usadas.append(atraccion)
            costo_total += calcular_precio(atraccion)
        else:
            print(f"No puede subir a la {atraccion}.")

    resumen = {
        "nombre": nombre,
        "edad": edad,
        "elegidas": elegidas,
        "usadas": usadas,
        "costo": costo_total
    }
    return resumen

def mostrar_resumen(resumen):
    print("--- RESUMEN DEL VISITANTE ---")
    print(f"Nombre: {resumen['nombre']}")
    print(f"Edad: {resumen['edad']} años")
    print(f"Atracciones elegidas: {resumen['elegidas']}")
    print(f"Atracciones permitidas: {resumen['usadas']}")
    print(f"Costo total: ${resumen['costo']}")