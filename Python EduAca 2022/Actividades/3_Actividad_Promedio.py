"""
Imagina que culminaste el 5º semestre de la universidad, en el cual viste las siguientes asignaturas:
 Seguridad Informática, Ingeniería Web, Inteligencia Artificial, Programación Móvil y Redes;
  y las notas fueron las siguientes: 5.0, 4.5, 3.6, 3.9 y 4.3 respectivamente.


Teniendo claro esto, escribe un programa que solicite tu nombre completo,
el nombre de las cinco materias y la calificación de cada una. Y como resultado devuelve tu nombre y el promedio obtenido en el semestre.



Recuerda que la fórmula para calcular el promedio es:

Promedio = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)/Cantidad de notas
"""
print("BIENVENIDO!")
nombre = input("Ingresar nombre y apellido: ")
materias = 5
contador = 1
totales = 0

while contador < materias:
    nombre_materia = input(f"Ingresar el nombre de la materia {contador}: ")
    nota = float(input(f"Ingresar la nota obtenida en {nombre_materia}: "))
    totales = totales + nota
    contador += 1
print (" ")
print(f"{nombre}, tu promedio en el 5to semestre es {(totales/materias)}")

# El nombre obtenido fue Perez Gerardo y su promedio fue de 2.6