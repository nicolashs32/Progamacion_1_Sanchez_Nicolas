def es_par(numero):
    return numero % 2 == 0

num = int(input(f"Ingrese un número: "))
if es_par(num):
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")

