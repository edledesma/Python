"""
Los diccionarios
Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value.
Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.
En el siguiente ejemplo tenemos tres keys que son ‘Nombre’: ‘Sara’, ‘edad’: 28, ‘Documento’. ‘456234’.



Y con esto hemos creado nuestro diccionario, ahora si quiero obtener uno de los datos almacenados,
entonces escribimos print(nombre_diccionario).



Debes saber que los diccionarios son flexibles, tanto que podemos utilizar distintas formas para crearlos.
Además, contiene métodos para insertar, limpiar, eliminar y devolver llaves y valores en forma de listas.



Para concluir esta clase, los diccionarios son mutables, es decir, es posible modificar su longitud, podemos agregar
o quitar elementos de él; de igual forma, todos los valores almacenados en el diccionario pueden ser modificados.



A diferencias de las listas y de las tuplas los diccionarios no se rigen por la regla de los índices, todos los valores
 que se almacenen en el diccionario no corresponden a un índice, sino a una llave.

Existen 3 formas para crear un diccionario
"""
#PRIMER FORMA


diccionario1 = {
    "Nombre" : "Sara",
    "Edad": 28,
    "Documento": 3526456
}

print(diccionario1)

#SEGUNDA FORMA


diccionario2 = dict(Nombre="Lara",
                   Edad=37,
                   Documento=3264944)


print(diccionario2)

#TERCERA FORMA

dicccionario3 = dict ([
    ("Nombre", "Mara"),
    ("Edad", 21),
    ("Documento", 3412515)
])

print(dicccionario3)

inventario = {"Manzanas": 235, "Peras": 300, "Naranjas": 250, "Sandias": 500}

# Si queremos ver las llaves (KEYS),en el ejemplo las categorias,  podemos usar el comando .keys
print(inventario.keys())
# Si queremos ver los valores (VALUES),en el ejemplo las cantidades,  podemos usar el comando .values
print(inventario.values())
# Si queremos ver los valores como items  podemos usar el comando .items
print(inventario.items())
