nombre = "Carlos"
tel = 111562648495
altura = 1.85

# Para imprimir los datos, los unimos mediante el operador +. Solamente podemos unir datos tipo cadena

print("Hola " + nombre + ", ¿como te encuentras?.")

# En el caso de la variable numerica, será necesario convertirla en cadena (STR)

print("Tu teléfono es " + str(tel))

""" Otra opción es colocando las cadenas F. Donde se coloca una F al principio del comando y las variables
se colocan entre { } . """

print(f"Hola {nombre} tu número es {tel}")

print(f"Hola {nombre}, tu número es {tel} y tu estatura es {altura}")
