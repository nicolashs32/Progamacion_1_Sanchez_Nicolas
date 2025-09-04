def buscar_mayor(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return a, b, c
        else:
            return a, c, b
    elif b >= a and b >= c:
        if a >= c:
            return b, a, c
        else:
            return b, c, a
    else:  # c es el mayor
        if a >= b:
            return c, a, b
        else:
            return c, b, a


# Programa principal
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

ordenados = buscar_mayor(n1, n2, n3)
print("Números ordenados de mayor a menor:", ordenados)