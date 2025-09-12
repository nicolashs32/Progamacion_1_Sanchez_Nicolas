
#2. Sumar todos los elementos:
#Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
#elementos.

def main():
    numeros = [0] * 10
    suma = 0

    for i in range(10):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))
        suma += numeros[i]

    print("La suma total es:", suma)

main()