# Definir el tipo PERSONA. 

class Identidad:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

#introducimos la edad con la función super para no tener que escribir de nuevo todos los datps

class Persona(Identidad):
    def __init__(self,nombre,apellido,edad):
        super().init(nombre,apellido,edad)
        self.edad=edad 

persona_1=Persona("Martina","Garcia","18")

#DEFINIR LA TABLA PERSONAS(imoportamos la libreria panda)
#El algoritmo está en el pseudocódigo

import pandas as pd

datos=[
    {"nombre":"Martina", "apellido":"Garcia","Edad":18},
    {"nombre":"Mario","apellido":"Sanchez","Edad":22},
    {"nombre":"Lucia","apellido":"Vázquez","Edad":45}
]

tabla_personas=pd.DataFrame(datos)

print(tabla_personas)

        
        