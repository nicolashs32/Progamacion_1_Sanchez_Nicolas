#10. Función para buscar la primera aparición de un valor:
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
#la posición de la primera aparición de ese número o -1 si no se encuentra.

def buscar(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

def main():
    numeros = [0] * 10

    for i in range(10):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    buscado = int(input("Ingrese el número a buscar: "))
    pos = buscar(numeros, buscado)

    if pos != -1:
        print(f"El número {buscado} se encuentra en la posición {pos+1}.")
    else:
        print("El número no se encuentra en la lista.")

main()
