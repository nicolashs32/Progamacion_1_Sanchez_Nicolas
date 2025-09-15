# Constantes
MAX_LIBROS = 20

# Listas inicializadas en blanco
titulos = [""] * MAX_LIBROS
ejemplares = [0] * MAX_LIBROS

# Variable para llevar el control de cuántos libros hay cargados
cantidad_libros = 0

while True:
    print("\n- MENÚ -")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catalogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (prestamo / devolucion)")
    print("7. Salir")

    opcion = input("Elija una opcion: ")

    # 1. Cargar títulos
    if opcion == "1":
        cant = int(input("¿Cuántos libros desea cargar? (máx 20): "))
        for i in range(cant):
            if cantidad_libros < MAX_LIBROS:
                titulo = input(f"Ingrese título {i+1}: ")
                cantidad = int(input("Ingrese cantidad de ejemplares: "))
                titulos[cantidad_libros] = titulo
                ejemplares[cantidad_libros] = cantidad
                cantidad_libros += 1
            else:
                print("Se alcanzó el máximo de libros permitidos (20).")
                break

    # 2. Mostrar catalogo
    elif opcion == "2":
        if cantidad_libros == 0:
            print("No hay libros cargados.")
        else:
            for i in range(cantidad_libros):
                print(f"{titulos[i]} → {ejemplares[i]} copias")

    # 3. Consultar disponibilidad
    elif opcion == "3":
        titulo_buscar = input("Ingrese el título a consultar: ")
        encontrado = False
        for i in range(cantidad_libros):
            if titulos[i] == titulo_buscar:
                print(f"{titulos[i]} → {ejemplares[i]} copias")
                encontrado = True
        if not encontrado:
            print("Libro no encontrado.")

    # 4. Listar titulos agotados
    elif opcion == "4":
        agotados = False
        for i in range(cantidad_libros):
            if ejemplares[i] == 0:
                print(f"{titulos[i]} esta agotado.")
                agotados = True
        if not agotados:
            print("No hay libros agotados.")

    # 5. Agregar un nuevo titulo
    elif opcion == "5":
        if cantidad_libros < MAX_LIBROS:
            nuevo_titulo = input("Ingrese el título del nuevo libro: ")
            cantidad = int(input("Ingrese cantidad de ejemplares: "))
            titulos[cantidad_libros] = nuevo_titulo
            ejemplares[cantidad_libros] = cantidad
            cantidad_libros += 1
            print("Libro agregado correctamente.")
        else:
            print(" No se puede agregar mas, ya hay 20 libros.")

