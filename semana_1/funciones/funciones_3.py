def area_triangulo(base, altura):
    return (base * altura) / 2

base = float(input(f"Ingrese la base del triángulo: "))
altura = float(input(f"Ingrese la altura del triángulo: "))
print(f"El área del triángulo es: {area_triangulo(base, altura)}")