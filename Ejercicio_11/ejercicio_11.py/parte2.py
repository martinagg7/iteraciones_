#APARTADO 2

#Estudiar una versión iterativa que calcula el mcd haciendo solo sumas o restas.

num_1 = int(input("Introduzca el primer numero:"))
num_2 = int(input("Introduzca el segundo numero:"))

def mcd_restas(num_1,num_2):
    if num_1>num_2:
        minuendo=num_1
        sustraendo=num_2
        diferencia=minuendo-sustraendo
        if diferencia==0:
            return sustraendo
        else:
            while diferencia!=0:
                if diferencia>sustraendo:
                    minuendo=diferencia
                    diferencia=minuendo-sustraendo
                else:
                    minuendo=sustraendo
                    sustraendo=diferencia
                    diferencia=minuendo-sustraendo  
            return sustraendo
    else:   
        minuendo=num_2
        sustraendo=num_1
        diferencia=minuendo-sustraendo
        if diferencia==0:
            return sustraendo
        else:
            while diferencia!=0:
                if diferencia>sustraendo:
                    minuendo=diferencia
                    diferencia=minuendo-sustraendo
                else:
                    minuendo=sustraendo
                    sustraendo=diferencia
                    diferencia=minuendo-sustraendo
            return sustraendo
             

print( "El mcd de",num_1,"y",num_2,"es",mcd_restas(num_1,num_2))
