#4. Contar mayores a un valor:
#Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

def main():
    numeros = [0] * 8
    contador = 0

    for i in range(8):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))
        if numeros[i] > 100:
            contador += 1

    print("Cantidad de números mayores a 100:", contador)

main()
