"""
Las funciones y estructuras de datos en python
Las funciones son bloques de códigos que realizan una tarea específica.
Son usadas en la programación, ya que nos permiten reutilizar código.

Por otro lado, las estructuras de datos nos permiten organizar los datos de
tal forma que su manipulación sea más sencilla.

--
FUNCIONES: Nos permite definir un bloque de código reutilizaba que se puede ejecutar muchas veces dentro de tu programa

ventajas:
- REDUCE EL NÚMERO TOTAL DE LÍNEAS
- FACILITA LA DEPURACIÓN
- LIMITAN LOS ERRORES DE ESCRITURA

Sentencia DEF

"""


def saludar():
    print("Hola mundo")


saludar()


def suma(a, b):
    resultado = a+b
    return resultado


print(suma(5, 6))


"""
-DEF es una palabra reservada que indica a Python que una nueva función está siendo definida.
-Luego viene una función con un nombre válido de tu elección, en este caso es suma.
    Es importante saber que los nombres de función no pueden ser palabras reservadas de Python
-A continuación los dos puntos (:) , los cuales finalizan la definición de la función.
-Consiguientemente, es necesaria una nueva línea, seguida por un nivel de indentación.
    La indentación es fundamental, permite a Python reconocer qué código pertenecerá a la función.
-Luego, llamamos return, este devuelve un valor específico, finalizando con esto la ejecución de la función.
-Por último, para ejecutar el código dentro de la función, tienes que hacer una invocación de la función.
"""
