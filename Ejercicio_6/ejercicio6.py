#Ejercicio 6: Historial de una cuenta corriente.

abrir_cuenta_corriente = input("¿Desea abrir una cuenta corriente? (S/N): ")
movimientos = 0
saldo = 0

if abrir_cuenta_corriente == "S":
    print("Bienvenido a su cuenta corriente.") 
    saldo = int(input("Introduzca el ingreso inicial: "))
    print("\n")
    movimientos = movimientos + 1

elif abrir_cuenta_corriente == "N":
    print("Gracias por su visita.")

else:
    print("Por favor, introduzca una opción válida.")

def operaciones(saldo, movimientos):
    operacion = input("¿Desea realizar una operación? (S/N): ")
    if operacion == "N":
        print("Su saldo actual es de " , saldo , "€. \n")

        total_operaciones = 20
        if movimientos > total_operaciones: 
            print("La media de movimientos es superior al indicado (20).º")
        else:
            print("La media de movimientos es inferior al indicado (20).")

        print("Gracias por su visita.")
            

    if operacion == "S":
        operacion = input("¿Que operacion desea realizar? (Ingreso/Retirada/Consultar): ")
        if operacion == "Ingreso":
            ingresar_mas_dinero = float(input("¿Cuánto dinero desea ingresar en su cuenta? "))
            saldo = saldo + ingresar_mas_dinero
            movimientos = movimientos + 1
            print("Su saldo actual es de " , saldo , "€. \n")
            return operaciones(saldo, movimientos)

        elif operacion == "Retirada":
            retirar_dinero = float(input("¿Cuánto dinero desea retirar de su cuenta? "))
            saldo = saldo - retirar_dinero
            movimientos = movimientos + 1

            if saldo < 0:
                print("Su cuenta está en números rojos: " , saldo , "€. \n")
                return operaciones(saldo, movimientos)
            elif saldo >= 0:
                print("Su saldo actual es de " , saldo , "€. \n")
                return operaciones(saldo, movimientos)

        elif operacion == "Consultar":
            print("Su saldo actual es de " , saldo , "€.    \n")
            return operaciones(saldo, movimientos)
        


operaciones(saldo, movimientos)