#APARTADO 1

# Dar una versión iterativa del algoritmo de Euclides para el cálculo del mcd de dos números enteros

num_1 = int(input("Introduzca el primer numero:"))
num_2 = int(input("Introduzca el segundo numero:"))

def euclides_mcd(num_1,num_2):
    if num_1>num_2:
        cociente=num_1//num_2
        resto=num_1%num_2
        if resto==0:
            return num_2
        else:
            while resto!=0:
                num_1=num_2
                num_2=resto
                cociente=num_1//num_2
                resto=num_1%num_2
            return num_2
    else:
        cociente=num_2//num_1
        resto=num_2%num_1
        if resto==0:
            return num_1
        else:
            while resto!=0:
                num_2=num_1
                num_1=resto
                cociente=num_2//num_1
                resto=num_2%num_1
            return num_1

        
       
print("El mcd de",num_1,"y",num_2,"es",euclides_mcd(num_1,num_2))
