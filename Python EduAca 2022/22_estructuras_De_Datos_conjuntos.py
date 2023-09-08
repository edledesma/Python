"""
En python un conjunto (set) es una estructura de datos que almacena elementos desordenados.
Los elementos del conjunto tampoco están indexados. Como una lista,
un conjunto permite la adición y eliminación de elementos.
Sin embargo, hay algunas características únicas que definen un conjunto y lo separan de otras estructuras de datos:
-Un conjunto no contiene elementos duplicados.
-Los elementos del conjunto son inmutables, es decir, no se pueden cambiar,
pero el conjunto en sí es mutable, es decir, se puede cambiar.
-Dado que los elementos del conjunto no están indexados, los conjuntos no admiten
operaciones de segmentación o indexación.

Métodos de los conjuntos:

add     - Añade un elemento al final del conjunto
clear   - Elimina toda la información del conjunto
pop     - Devuelve y elimina un elemento arbitrario o devuelve un error si está vacío
remove  - Intente eliminar un elemento del conjunto, si no existe eleve un error
union   - Devuelve un conjunto con todos los elementos de ambos conjuntos

"""
# PRIMERA FORMA DE CREAR CONJUNTOS
alumnos = {"Andre", "Ruby", "Marcos", "Mario"}
print(type(alumnos))
print(alumnos)

# SEGUNDA FORMA DE CREAR CONJUNTOS
lenguajes = set(["PHP", "JAVA", "C", "PYTHON"])
print(lenguajes)
lenguajes.add("C#")
lenguajes.pop()
lenguajes.remove("JAVA")
print(lenguajes)

todos = alumnos.union(lenguajes)
print(todos)
