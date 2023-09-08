# Los condicionales - Son if (Si) , else (Si no) y elif (Si no,si)

# Elif - En el Elif las condiciones son evaluadas en orden, procediendo a la proxima solo si el resultado de la anterior
# fue falso.

"""
Ejemplo 1: Acorde a la edad del usuario se determina que tipo de registro puede sacar
Cond 1: menor a 16, no puede conducir
Cond 2: menor a 18, puede conducir
Cond 3: menor a 70, licencia standard
Cond 3: mayor a 70, licencia especial
"""

edad = int(input("Ingresa tu edad: "))

if edad < 16:
    print("No apto para conducir")
elif edad < 18:
    print("Puede conducir")
elif edad < 70:
    print("Puede obtener licencia standard")
else:
    print("Puede obtener licencia especial")

# En este ejemplo podemos colocar todas las cantidades de ELIF que nos sean necesarios,
# siempre debajo del IF y arriba del ELSE.
