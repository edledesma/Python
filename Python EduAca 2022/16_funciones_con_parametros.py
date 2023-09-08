"""
En primer lugar, debemos recalcar que los parámetros son valores que enviamos cuando invocamos la función y nos
permiten realizar operaciones dentro de la función.


En Python se pueden definir parámetros y asignarles un dato en la misma cabecera de la función.
Luego, cuando llamamos a la función podemos o no enviarle un valor al parámetro.
En la siguiente imagen puedes ver la sintaxis para declarar funciones con parámetros:

def nombre (param1,param2):
    inst1
    inst2

    return valor
EJEMPLO 1:

def es_par(numero):
    if numero % 2 == 0:
        print(f"{numero} Es par")
    else:
        print(f"{numero} es impar")


es_par(10)


EJEMPLO 2:

def saludar(nombre):
    print(f"Hola {nombre}, eres el mejor programador")


saludar("Marcos")

EJEMPLO 3:



def resta(a=None, b=None):
    if a == None or b == None:
        print("Error debes enviar dos números")
        return
    return a-b


resultado = resta(1, 99)


print(resultado)



EJEMPLO 4:
"""
def multi(numero= None):
    if numero == None:
        print("Por favor introduce un número")
    else:
        print(f"Tabla de multiplicar de {numero}")
        for i in range(1, 11):
            print(f"{i} x {numero} = {i*numero}")

multi(0)

"""
Es importante mencionar que las funciones con parámetros se definen de la misma manera, colocamos la palabra 
def luego el nombre de la función y los paréntesis.
 
En conclusión, de esta forma podemos crear funciones útiles que podamos usar más de una vez en el programa. 
Decir que, una función creada por nosotros,
puede recibir todos los parámetros que queramos, pero siempre habrá que indicarlo correctamente en la declaración.

"""
