#APARTADO 2

#Escribir el algoritmo de cálculo de la raíz cuadrada entera de un número entero.

def raiz_cuadrada(n):
    r=0
    if n<0:
        return "No se puede calcular la raiz cuadrada de un numero negativo"
    if n>=0:
        while r*r<n:
            r=r+1
        if r*r==n:
            return r
        else:
            return "No existe raiz cuadrada exacta"

n=int(input("Introduzca un numero:"))