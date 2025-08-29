

print(f"Bienvenidos a PythonLand! Por favor ingrese los siguientes datos e intereses: ")
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
print(f"Perfecto!, estos son nuestros precios: Montaña Rusa = $1500, Casa del Terror = $1200, Carrusel = $800 ")


atraccion=int(input("A cuál de las siguientes atracciones le gustaría entrar? (1-montaña rusa ; 2-Casa del Terror ; 3- Carrusel) "))

while atraccion!=1 and atraccion!=2 and atraccion!=3:
    print(f"Error, opción no valida!")
    atraccion=int(input("A cuál de las siguientes atracciones le gustaría entrar? (1-montaña rusa ; 2-Casa del Terror ; 3- Carrusel) "))

entrada=0
atraccion_elegida=""
contador_montaña = 0
contador_terror = 0
contador_carrusel = 0


while True:
    if edad<=6 and atraccion!=3:
        print("Solo tiene edad para entrar al carrusel ")
        atraccion=int(input("Elija nuevamente (3-Carrusel)"))
        continue
    elif edad<=12 and atraccion==1:
        print("Error, usted solo puede pasar al Carrusel y Casa del Terror ")
        atraccion=int(input("Elija nuevamente (2-Casa del Terror o 3-Carrusel"))
        continue
    else:
        print("Pase por favor. ")

    if atraccion==1:
        entrada+=1500
        atraccion_elegida+="Montaña Rusa"
        contador_montaña+=1
    elif atraccion==2:
        entrada+=1200
        atraccion_elegida+="Casa del Terror"
        contador_terror+=1
    else:
        entrada+=800
        atraccion_elegida+="Carrusel"
        contador_carrusel+=1

    repetir = input("Espero que lo haya disfrutado!! ¿Le gustaría ir a otra atracción? (s/n) ")

    while repetir != "s" and repetir != "n":
        print("Error, opción no válida. Responda con 's' o 'n'.")
        repetir = input("¿Le gustaría ir a otra atracción? (s/n) ")

    if repetir == "n":
        break
    else:
        atraccion = int(input("A cuál de las siguientes atracciones le gustaría entrar? (1-Montaña Rusa ; 2-Casa del Terror ; 3-Carrusel) "))
    while atraccion != 1 and atraccion != 2 and atraccion != 3:
        print("Error, número incorrecto, vuelva a seleccionar")
        atraccion = int(input("A cuál de las siguientes atracciones le gustaría entrar? (1-Montaña Rusa ; 2-Casa del Terror ; 3-Carrusel) "))


print(f"Su ticket es: ")

print(f"Nombre: ",nombre)

print(f"Edad: ", edad)

print(f"Cantidad de veces subido al carrusel: ", contador_carrusel)

print(f"Cantidad de veces que entró a la Casa del Terror: ", contador_terror)

print(f"Cantidad de veces que subió a la Montaña Rusa: ", contador_montaña)

print(f"Total a pagar: ", entrada)


