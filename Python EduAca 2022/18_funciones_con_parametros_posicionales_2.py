"""
def lenguaje(nombre, *args):
    print(f"Hola {nombre}\nTus lenguajes favoritos son : {args}")


lenguaje("David", "Ruby", "Python")
"""


def lenguaje(nombre, **kwargs):
    print(f"Hola {nombre}\nBuscando información acerca de tus lenguajes favoritos.\nCargando Información...\n")
    print("Información: ")
    contador = 0
    for i in kwargs:
        contador += 1
        print(f"Tu {contador} lenguaje favorito es: {kwargs[i]}")


lenguaje("David", lenguaje1="Ruby", lenguaje2="Python", lenguaje3="Java", lenguaje4="PHP", )
