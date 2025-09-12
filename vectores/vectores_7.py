#7. Invertir orden:
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.

def main():
    numeros = [0] * 6

    for i in range(6):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    print("Array invertido:")
    for i in range(5, -1, -1):
        print(numeros[i])

main()
