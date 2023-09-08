"""
Las tuplas

Las tuplas en Python son muy similares a las listas, pero con dos diferencias.
Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse
con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.


La gran ventaja que ofrecen las tuplas es el poco espacio que ocupan en memoria, dado que al ser inmutables,
no necesitan reservar espacio adicional, como en el caso de las listas.


Las tuplas ofrecen el método count para contar los elementos e index para devolver el índice de un elemento.
 A continuación, veremos un ejemplo:
"""
numeros = (5, 6, 7, 8, 9, 12, 14, 90, 12)

variable1 = int(input("Dame un numero: "))

print("El número se repite: "+ str(numeros.count(variable1)) + " veces.")
print("El número " +str(variable1) + " se encuentra en la posición " + str(numeros.index(variable1)))