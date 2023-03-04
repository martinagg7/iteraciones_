#ENVEJECER UN AÑO

import pandas as pd
datos=[
    {"nombre":"Martina", "apellido":"Garcia","Edad":18,"Padres":"si"},
    {"nombre":"Mario","apellido":"Sanchez","Edad":22,"Padres":"si"},
    {"nombre":"Lucia","apellido":"Vázquez","Edad":12,"Padres":"Huerfano"},
    {"nombre":"Sara","apellido":"Sánchez","Edad":10,"Padres":"Huerfano"}
]   

tabla_personas=pd.DataFrame(datos)

tabla_personas['edad']+=1
print(tabla_personas)