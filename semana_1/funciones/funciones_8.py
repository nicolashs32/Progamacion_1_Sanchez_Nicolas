
def calcular_edad(año):
    return 2025 - año


año = int(input("Ingrese su año de nacimiento: "))

edad = calcular_edad(año)
print(f"Tu edad es: {edad} años")