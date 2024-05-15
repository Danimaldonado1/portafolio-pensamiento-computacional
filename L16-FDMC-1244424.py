# Semana No. 16: Ejercicio 1

print("Semana No. 16: Ejercicio 1")


import random

arreglo = []

for i in range(10):
    numero = random.randint(0, 100)
    arreglo.append(numero)

print("\nNúmeros ingresados:")
print(arreglo)


promedio = sum(arreglo) / len(arreglo)
print(f"\nPromedio del arreglo: {promedio}")

print(f"Longitud del arreglo: {len(arreglo)}")


suma_pares = 0
for i in range(0, len(arreglo), 2):
    suma_pares += arreglo[i]

print(f"Suma de posiciones pares: {suma_pares}")


suma_impares = 0
for i in range(1, len(arreglo), 2):
    suma_impares += arreglo[i]

print(f"Suma de posiciones impares: {suma_impares}")


# Ejercicio 2

print("Semana No. 16: Ejercicio 2")


filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz = []


import random

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = random.randint(0, 1000)
        fila.append(numero)
    matriz.append(fila)


print("\nMatriz:")
for fila in matriz:
    print(fila)

pares = 0
impares = 0
mayor = matriz[0][0]
menor = matriz[0][0]

for fila in matriz:
    for numero in fila:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > mayor:
            mayor = numero

        if numero < menor:
            menor = numero


print("\nEstadísticas:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")