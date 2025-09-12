#5. Buscar un valor:
#Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
#Informar la posición en caso afirmativo, o indicar que no se encuentra.

def main():
    numeros = [0] * 10

    for i in range(10):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    buscado = int(input("Ingrese el número a buscar: "))
    encontrado = -1

    for i in range(10):
        if numeros[i] == buscado:
            encontrado = i
            break

    if encontrado != -1:
        print(f"El número {buscado} se encuentra en la posición {encontrado}.")
    else:
        print("El número no se encuentra en el array.")

main()