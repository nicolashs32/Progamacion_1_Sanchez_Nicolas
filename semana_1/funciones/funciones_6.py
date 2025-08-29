def convertir_minutos(minutos):
    horas = minutos // 60
    resto = minutos % 60
    return horas, resto

minutos = int(input(f"Ingrese la cantidad de minutos: "))
h, m = convertir_minutos(minutos)
print(f"{minutos} minutos equivalen a {h} horas y {m} minutos")
