# Clase Persona
#Atributo DNI , NOMBRE ,APELLIDO, 
#Metodos __init__ , __str__

class Persona():
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"DNI: {self.dni},\nNombre: {self.nombre}\nApellido: {self.apellido}"

class Alumno(Persona):
    def __init__(self,dni,nombre,apellido,legajo):
        super().__init__(dni,nombre,apellido) #Llama al constructor de la clase padre.
        self.legajo = legajo
        

    def __str__(self):
        return super().__str__() + f"\Legajo: {self.legajo}"
    
class Curso():
    def __init__(self, idcurso,docente):
        self.idcurso = idcurso
        self.docente = docente
        self.lista = []

    def __str__(self):
        cad= f"Id: {self.idcurso}\nDocente: {self.docente}\n" 
        for alumno in self.lista:
            cad+=alumno.__str__()+"\n"
        return cad
    
    def agregar_alumnos(self, Alumno):
        self.lista.append(Alumno)




#Programa

n=int(input("Ingresar cantidad de alumnos: "))
idcurso=input("Ingrese el id del curso: ")
docente=input("Ingrese el docente: ")

objeto_curso=Curso(idcurso,docente)

for i in range(n):

    dni=int(input("Ingrese el DNI: "))
    nombre=input("Ingrese el nombre: ")
    apellido=input("Ingrese el apellido: ")
    legajo=i
    objeto_alumno = Alumno(dni, nombre, apellido, legajo)
    objeto_curso.agregar_alumnos(objeto_alumno)
    
print(objeto_curso)




