#Ejercicio 7: Edición de un número entero.

def cambio_de_base(numero, base):
    if base<2:
        print("La base debe ser mayor o igual a 2.")
    
    elif base>36:
        print(numero)

    else:
        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        resultado = ""
        while numero > 0:
            resto = numero % base
            resultado = digitos[resto] + resultado
            numero = numero // base
        print(resultado)

def main():
    base = int(input("Introduce la base mayor o igual a 2: "))
    numero = int(input("Escriba un numero: "))
    cambio_de_base(numero, base)

if __name__ == "__main__":
    main()