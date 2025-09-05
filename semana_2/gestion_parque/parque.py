# gestion_parque/parque.py

def mostrar_atracciones():
    print("Genial!! Nuestros precios son los siguientes:")
    print("1 - Montaña Rusa = $1500")
    print("2 - Casa del Terror = $1200")
    print("3 - Carrusel = $800")

def puede_subir(edad, atraccion):
    if edad <= 6 and atraccion != 3:
        return False
    if edad <= 12 and atraccion == 1:
        return False
    return True

def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0

def registrar_visita():
    print("---Bienvenidos a PythonLand!---")
    print("Por favor complete los siguientes datos")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    entrada = 0
    contador_montaña = 0
    contador_terror = 0
    contador_carrusel = 0

    while True:
        mostrar_atracciones()
        atraccion = int(input("A cuál atracción desea entrar (1-3): "))

        # Validación de opción
        while atraccion != 1 and atraccion != 2 and atraccion != 3:
            print("Error, opción no válida!")
            atraccion = int(input("Elija (1-Montaña Rusa ; 2-Casa del Terror ; 3-Carrusel): "))

        # Validación de edad
        while not puede_subir(edad, atraccion):
            print("No cumple la edad para esa atracción.")
            atraccion = int(input("Elija otra atracción (1-3): "))

        # Registrar atracción
        entrada += calcular_precio(atraccion)

        if atraccion == 1:
            contador_montaña += 1
        elif atraccion == 2:
            contador_terror += 1
        else:
            contador_carrusel += 1

        # Preguntar si quiere otra
        repetir = input("¿Le gustaría subir a otra atracción? (s/n) ")
        while repetir != "s" and repetir != "n":
            repetir = input("Error, responda con 's' o 'n': ")

        if repetir == "n":
            break

    # Diccionario con la info
    resumen = {
        "nombre": nombre,
        "edad": edad,
        "montaña": contador_montaña,
        "terror": contador_terror,
        "carrusel": contador_carrusel,
        "total": entrada
    }

    return resumen

def mostrar_resumen(resumen):
    print("\n--- Este es su ticket. Gracias por su visita! ---")
    print("Nombre:", resumen["nombre"])
    print("Edad:", resumen["edad"])
    print("Cantidad de veces subido al Carrusel:", resumen["carrusel"])
    print("Cantidad de veces que entró a la Casa del Terror:", resumen["terror"])
    print("Cantidad de veces que subió a la Montaña Rusa:", resumen["montaña"])

    if resumen["montaña"] == 0:
        print("No subió a la Montaña Rusa")
    if resumen["terror"] == 0:
        print("No entró a la Casa del Terror")
    if resumen["carrusel"] == 0:
        print("No subió al Carrusel")

    print("TOTAL A PAGAR:", resumen["total"])