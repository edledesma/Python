"""
LISTAS
TUPLAS
DICCIONARIOS
CONJUNTOS

Las listas:

Las listas en Python son variables que almacenan “arreglos” arrays, Objetos, donde internamente cada posición
puede ser un tipo de datos distinto. A continuación, veremos un ejemplo de listas:

Lista = ["Elemento 1","Elemento 2","Elemento 3","Elemento 4"]

En el ejemplo, podemos observar que una lista no es únicamente un arreglo de varios objetos. Además, es una
colección ordenada de objetos, es decir que el primer elemento comenzará siempre con la dirección
o índice cero (0), el segundo elemento con 1 y así sucesivamente.



Algunas propiedades de las listas:
-Ordenadas, Mantienen el orden en el que han sido definidas.
-Dinámicas, Se pueden añadir o eliminar elementos.

EJEMPLO 1:

asignaturas = ["Matemáticas", "Física", "Español", "Ingles"]
print(asignaturas[1])
print(type(asignaturas))

EJEMPLO 2:

# CON EL METODO APPEN AGREGAMOS ELEMENTOS A LISTA Y CON SORT LOS ORDENAMOS

numeros = []
for i in range(6):
    numeros.append(int(input("Introduce un número:")))

numeros.sort()
print(f"Los números ganadores son: {numeros}")

EJMPLO 3:
"""




lista = [1,1,4,5,6,9,8,"David","David",]

# CON EL MÉTODO REMOVE QUITAMOS EL PRIMER ELEMENTO DE LA LISTA QUE COINCIDIA CON EL PARAMETRO
lista.remove("David")
# CON EL MÉTODO POP QUITAMOS EL ELEMENTO EN EL INDICE MARCADO.
lista.pop(3)
# CON EL MÉTODO DEL PONEMOS EL NOMBRE DE LA LISTA Y INDICAMOS EL INDICE A ELIMINAR.
del lista[1]
# CON EL MÉTODO CLEAR ELIMINAMOS POR COMPLETO TODA LA LISTA.
# lista.clear()

print(lista.count(7))
for i in lista:
    print(i)

#   CON EL MÉTODO INDEX NOS INDICA EL INDICE EN EL QUE ESTA UN ELEMENTO
print(lista.index(9))
#   CON EL MÉTODO REVERSE INVERTIMOS EL ORDEN DE LA LISTA
lista.reverse()
print(lista)

