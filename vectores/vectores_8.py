#8. Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales.

def main():
    a = [0] * 5
    b = [0] * 5
    iguales = True

    print("Ingrese los numeros de la prinera lista: ")
    for i in range(5):
        a[i] = int(input(f"Numero {i+1}: "))

    print("Ingrese los numeros de la segunda lista: ")
    for i in range(5):
        b[i] = int(input(f"Numero {i+1}: "))

    for i in range(5):
        if a[i] != b[i]:
            iguales = False
            break

    if iguales:
        print("Las listas son iguales.")
    else:
        print("Las listas NO son iguales.")

main()