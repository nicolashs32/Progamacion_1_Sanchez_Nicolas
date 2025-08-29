def verificar_acceso(edad):
    return edad >= 18

edad = int(input(f"Ingrese su edad: "))
if verificar_acceso(edad):
    print(f"Acceso permitido. Con {edad} años eres mayor de edad.")
else:
    print(f"Acceso denegado. Con {edad} años eres menor de edad.")