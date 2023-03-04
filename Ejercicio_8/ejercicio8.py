
#Ejercicio 8: Análisis de una cadena de caracteres.

import tabulate

def descomponer():
    separador = input("Introduce el separador que desea utilizar: ")
    cadena = input("Introduce un texto para analizar: ")
    ca = cadena.split(separador)
    lista = []

    for i in range(0, len(ca)):
        lista.append(list(ca[i:i+1]))
    
    print(tabulate.tabulate(lista, headers=["Palabra", "Longitud"], tablefmt = "fancy_grid", showindex = True))


descomponer()