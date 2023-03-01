#APARTADO 1

# Hacer un algoritmo que establezca la lista de los cuadrados perfectos inferiores a un límite dado. El algoritmo no debe hacer multiplicaciones.

def cuadrados_perfectos(limite):
    n = 1
    cuadrado = n
    lista_cuadrados = []
    while cuadrado <= limite:
        lista_cuadrados.append(cuadrado)
        n =n+1
        cuadrado = n + n - 1 + cuadrado
    return lista_cuadrados
limite=int(input("Introduzca el limite para los cuadrados:"))

print(cuadrados_perfectos(limite))