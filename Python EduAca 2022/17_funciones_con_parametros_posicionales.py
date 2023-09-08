"""

Al declarar una función podemos definir una serie de parámetros con lo que invocar a dicha función. Por regla general
el número y el nombre de estos parámetros es inmutable. Por ejemplo, si definimos 2 parámetros no podemos agregar más.

En primer lugar, debemos recalcar que cuando pasamos un argumento a una función directamente y
se asigna a un parámetro en función de su posición, se denomina argumento posicional.
 Así mismo, al declarar una función podemos definir una serie de parámetros con los que invocamos a dicha función,
 pero por regla general el número y el nombre de estos parámetros es inmutable, es decir que si defino
 que tendrá dos parámetros, entonces no podría agregar más.



En python, existen dos tipos de parámetros posicionales:



El principal uso de *args y **kwargs es en la definición de funciones.
Ambos permiten pasar un número variable de argumentos a una función,
 por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable,
 considera la utilización de *args o **kwargs como una opción. De hecho, el nombre de args viene de argumentos,
 que es como se denominan en programación a los parámetros de entrada de una función.


A modo de conclusión, recuerda que *args recibe los argumentos como una tupla y el **kwargs los
recibe como un diccionario. Por otro lado, usar estos parámetros puede ahorrarte mucho tiempo a la hora de programar.
"""


def suma(*args):
    total_suma = 0
    for i in args:
        total_suma += i
    return total_suma


resultado = suma(3, 4, 5, 6, 6, 7)
print(resultado)
