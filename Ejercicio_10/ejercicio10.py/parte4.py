
#LISTA DE LOS HUERFANOS DE MENOS DE 15
import pandas as pd
datos=[
    {"nombre":"Martina", "apellido":"Garcia","Edad":18,"Padres":"si"},
    {"nombre":"Mario","apellido":"Sanchez","Edad":22,"Padres":"si"},
    {"nombre":"Lucia","apellido":"Vázquez","Edad":45,"Padre":"Huerfano"},
    {"nombre":"Sara","apellido":"Sánchez","Edad":10,"Padres":"Huerfano"}
]

tabla_personas=pd.DataFrame(datos)

condición=(tabla_personas["Padres"]=="Huerfano")& (tabla_personas["Edad"]<15)
personas_huerfanas_menos_15=tabla_personas[condición]

print(personas_huerfanas_menos_15)
