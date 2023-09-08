"""
print("Howdy chaps")
print("Welcome to fullstack python")

nombre="Ana" 
apellido="Paz"
edad=25
altura=1.50
altura=150



nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad = int(input("Ingresar edad: "))
altura = float(input("Ingresar altura: "))


nombre_completo= nombre+" "+apellido

print(f' {nombre_completo} tiene {edad} años , su altera es {altura}')


"""

numeros= {10,5}

def suma_numero(numeros):
    suma=0
    for numero in numeros:
        suma+=numero
    return suma

print(suma_numero(numeros))
