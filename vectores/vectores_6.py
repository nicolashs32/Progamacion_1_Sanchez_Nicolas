#6. Mayor y su posición:
#Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
#encuentra.

def main():
    numeros = [0] * 7

    for i in range(7):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    mayor = numeros[0]
    pos = 0

    for i in range(1, 7):
        if numeros[i] > mayor:
            mayor = numeros[i]
            pos = i

    print(f"El mayor es {mayor} y está en la posición {pos}.")

main()