
# Diccionario de atracciones con precios
atracciones = {
    1: ("Montaña Rusa", 1500),
    2: ("Casa del Terror", 1200),
    3: ("Carrusel", 800)
}

def mostrar_atracciones():
    print("Atracciones disponibles:")
    print("1. Montaña Rusa - $1500")
    print("2. Casa del Terror - $1200")
    print("3. Carrusel - $800")

def puede_subir(edad, atraccion):
    if atraccion == "Montaña Rusa" and edad < 12:
        return False
    if atraccion != "Carrusel" and edad < 6:
        return False
    return True

def calcular_precio(atraccion):
    for opcion, datos in atracciones.items():
        nombre, precio = datos
        if nombre == atraccion:
            return precio
    return 0

def registrar_visita():
    nombre = input("Ingrese el nombre del visitante: ")
    edad = int(input("Ingrese la edad del visitante: "))
    cant_atracciones = int(input("¿Cuántas atracciones desea usar? (máx 3): "))

    atracciones_elegidas = ""
    atracciones_permitidas = ""
    costo_total = 0

    mostrar_atracciones()

    for i in range(cant_atracciones):
        opcion = int(input(f"Seleccione la atracción {i+1} (1-3): "))
        atraccion, _ = atracciones[opcion]

        atracciones_elegidas += atraccion + " "

        if puede_subir(edad, atraccion):
            print(f"Puede subir a la {atraccion}.")
            atracciones_permitidas += atraccion + " "
            costo_total += calcular_precio(atraccion)
        else:
            print(f"No puede subir a la {atraccion}.")

    resumen = {
        "nombre": nombre,
        "edad": edad,
        "elegidas": atracciones_elegidas,
        "permitidas": atracciones_permitidas,
        "costo_total": costo_total
    }
    return resumen

def mostrar_resumen(resumen):
    print("--- RESUMEN DEL VISITANTE ---")
    print(f"Nombre: {resumen['nombre']}")
    print(f"Edad: {resumen['edad']} años")
    print(f"Atracciones elegidas: {resumen['elegidas']}")
    print(f"Atracciones permitidas: {resumen['permitidas']}")
    print(f"Costo total: ${resumen['costo_total']}")