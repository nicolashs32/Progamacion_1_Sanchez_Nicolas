def buscar_mayor(n1, n2, n3):
    return sorted([n1, n2, n3], reverse=True)

x = float(input(f"Ingrese el primer número: "))
y = float(input(f"Ingrese el segundo número: "))
z = float(input(f"Ingrese el tercer número: "))
print(f"Números ordenados de mayor a menor: {buscar_mayor(x, y, z)}")