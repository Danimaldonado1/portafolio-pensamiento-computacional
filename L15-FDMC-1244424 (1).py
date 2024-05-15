# Semana No. 12: Ejercicio 1

print("Semana No. 12: Ejercicio 1")

def ObtenerAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

def ObtenerAreaCuadrado(lado):
    area = lado ** 2
    return area

def ObtenerAreaRectangulo(base, altura):
    area = base * altura
    return area

def ObtenerAreaCírculo(radio):
    import math
    area = math.pi * (radio ** 2)
    return area

# Menú de opciones
print("\nSeleccione la opción que desea calcular:")
print("a. Área de triángulo")
print("b. Área de cuadrado")
print("c. Área de rectángulo")
print("d. Área de círculo")

opcion = input("Ingrese la letra correspondiente a la opción deseada: ")

# calcular el área según la opción elegida
if opcion == "a":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = ObtenerAreaTriangulo(base, altura)
    print(f"El área del triángulo es: {area}")
elif opcion == "b":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = ObtenerAreaCuadrado(lado)
    print(f"El área del cuadrado es: {area}")
elif opcion == "c":
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = ObtenerAreaRectangulo(base, altura)
    print(f"El área del rectángulo es: {area}")
elif opcion == "d":
    radio = float(input("Ingrese el radio del círculo: "))
    area = ObtenerAreaCírculo(radio)
    print(f"El área del círculo es: {area}")
else:
    print("Opción inválida.")


# Semana No. 12: Ejercicio 2

print("Semana No. 12: Ejercicio 2")

# Coordenadas globales
x = 0
y = 0

def MoverHaciaArriba():
    global y
    y += 1

def MoverHaciaAbajo():
    global y
    y -= 1

def MoverHaciaLaDerecha():
    global x
    x += 1

def MoverHaciaLaIzquierda():
    global x
    x -= 1

while True:
    #  menú
    print("\nSeleccione una opción:")
    print("a. Sube")
    print("b. Baja")
    print("c. Izquierda")
    print("d. Derecha")
    print("e. Salir")

    opcion = input("Ingrese la letra correspondiente a la opción deseada: ")

    # opción seleccionada
    if opcion == "a":
        MoverHaciaArriba()
        print(f"Coordenadas actuales: {x},{y}")
    elif opcion == "b":
        MoverHaciaAbajo()
        print(f"Coordenadas actuales: {x},{y}")
    elif opcion == "c":
        MoverHaciaLaIzquierda()
        print(f"Coordenadas actuales: {x},{y}")
    elif opcion == "d":
        MoverHaciaLaDerecha()
        print(f"Coordenadas actuales: {x},{y}")
    elif opcion == "e":
        print(f"Coordenadas finales del personaje: {x},{y}")
        break
    else:
        print("Opción inválida. Intente nuevamente.")