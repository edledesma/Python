# Los condicionales - Son if (Si) , else (Si no) y elif (Si no,si)

#If y else
"""
El If evalúa la condición. Debe estar presente.
Por otro lado, el Else especifica que hacer si no se cumple la condición y es totalmente opcional.
En una condición no puede haber más de dos else.

Ejemplo:
Crear un programa que pregunta la edad del usuario y que exprese si es mayor de edad o menor.
"""

edad = int(input("¿Cual es tu edad?: "))
if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
print("Adios")