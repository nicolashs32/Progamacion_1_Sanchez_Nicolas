#1. Cargar y mostrar array:
#Declarar un array de 5 enteros. Cargarlo por teclado y mostrar su contenido por pantalla usando un
#ciclo for.

def main():
    numeros = [0] * 5  

    for i in range(5):
        numeros[i] = int(input(f"Ingrese el número {i+1}: "))

    print("Sus numeros son: ")
    for i in range(5):
        print(numeros[i])

main()
