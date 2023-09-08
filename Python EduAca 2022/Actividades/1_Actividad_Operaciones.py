"""
El día de hoy, tienes el reto de implementar un programa muy sencillo basado en la línea de comandos.
Su programa deberá aceptar las entradas de esta manera:

Ingresa el primer número: 3
Ingresar el segundo número: 4

Después, con los números ingresados (3 y 4) deberá mostrar los siguientes resultados:

3 + 4 = 7

3 * 4 = 12

3 == 4 : false

3 < 4 : true

4 >= 3 : true
"""


numero1 = int(input("Ingresar primer valor: "))
numero2 = int(input("Ingresar segundo valor: "))
print(f"El resultado de la suma es {numero1 + numero2}")
print(f"El resultado de la multiplicacion es {numero1 * numero2}")
print(f"¿Los números son iguales? {numero1 == numero2}")
print(f"¿Número 1 es menor? {numero1 < numero2}")
print(f"¿Número 1 es mayor o igual? {numero1 >= numero2}")
