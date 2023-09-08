
#____________Ejemplo 1________________#


#atributos nom dni tel edad
#metodo mostrar_datos, constructor, es_mayor_edad

class Persona():

    def __init__ (self, nombre,dni,tel,edad): #Constructor de la clase
        self.nombre = nombre
        self.dni = dni
        self.tel = tel
        self.edad = edad



    def __str__(self): #Metodo especial de python para mostar datos
        return(f"Nombre: {self.nombre}\nDNI: {self.dni}\nTel: {self.tel}\nEdad: {self.edad}\nMayor de edad: {self.es_mayor_edad()}")

    def es_mayor_edad(self):
        return self.edad>=18

#Programa principal 

p1 = Persona("Ana",222222,"35353535",30)

"""""
print(p1)


nombre = input("Ingrese el nombre: ")
dni = int(input("Ingrese el dni: "))
tel = input("Ingrese el telefono: ")
edad = int(input("Ingrese la edad: "))

p2=Persona(nombre,dni,tel,edad)

print(p2)

"""

#____________Ejemplo 2________________#

#atributos base y altura
#metodos constructor (__init___), mostrar datos (__str__), calcular perimetro y superfico

class Rectangulo():

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def __str__(self):
        return (f"La altura es {self.altura} y la base es {self.base}")
