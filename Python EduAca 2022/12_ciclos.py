# Los ciclos optimizan el código permitiendo ejecutar un bloque de código varias veces mientras se
# cumpla determina condición.
"""
Disminuir la cantidad de instrucciones a usar
Reducir el tamaño del programa
Programar con mayor rapidez
"""
# Existen dos tipos de ciclos, FOR & WHILE

"""
Consta de 3 partes. 
- La variable 
- IN - Palabra reservada, es decir siempre va
- El elemento - Es el que se va a iterar

#Ciclo For
for i in elemento:
print ("Hola", variable1)

"""
# Ejemplo 1 - Imprime una palabra 10 veces.
word = input("Ingresar una palabra: ")
for i in range(10):
    print (word)

# Ejemplo 2 - Realiza el cuadrado de los números y muestra las cantidades de vueltas.
print("Comienzo")

contador = 1

for i in [3,4,5,6,7,8]:
    print(f"Vuelta numero: {contador}")
    print(f"Hola, ahora i vale {i} y su cuadrado es {i ** 2}")
    contador += 1

print("Adios")

