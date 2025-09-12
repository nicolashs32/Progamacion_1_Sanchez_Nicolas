#3. Promedio de valores:
#Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
#de los valores.


def main():
    numeros = [0.0] * 6
    suma = 0.0

    for i in range(6):
        numeros[i] = float(input(f"Ingrese el numero {i+1}: "))
        suma += numeros[i]

    promedio = suma / 6
    print("El promedio es:", promedio)

main()