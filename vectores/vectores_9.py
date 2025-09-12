#9. Intercambiar elementos pares por ceros:
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
#resultante.

def main():
    numeros = [0] * 10

    for i in range(10):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    for i in range(10):
        if numeros[i] % 2 == 0:
            numeros[i] = 0

    print("Resultado:")
    for i in range(10):
        print(numeros[i])

main()

