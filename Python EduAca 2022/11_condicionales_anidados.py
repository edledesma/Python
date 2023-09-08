# Los condicionales - Son if (Si) , else (Si no) y elif (Si no,si)

# If anidados - Un If dentro de otro If.

"""
Ejemplo 1: Pedir edad y preguntar si se graduó. Si es mayor Y se graduó muestra el mensaje.
"""

edad = int(input("Ingresar edad: "))


if edad > 18:
    grad = input("¿Ya te graduaste?: ")
    print ("Felicidades! Sos mayor")
    if grad == "si" or grad == "Si":
        print("Felicidades por tu graduación!")
    else:
        print("Seguí trabajando en el título")
else:
    print("Volvé cuando seas mayor")



"""
Ejemplo 2: Pedir contraseña, evaluar que tenga 8 o más caracteres y revisar que sea equivalente a "Prueba12345"
"""

password = input("Ingresar contraseña: ")

if (len(password) >= 8):
    print("CONTRASEÑA ACEPTABLE")
    if (password == "Prueba12345"):
        print("Es correcta")
    else:
        print("Pero es incorrecta")
else:
    print("Contraseña incorrecta e insegura")
