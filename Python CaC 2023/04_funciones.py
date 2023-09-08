"""
def suma(a,b):
    return a+b

a = int(input("Ingresar primer valor: "))
b = int(input("Ingresar segundo valor: "))

print(f"La suma es {suma(a,b)}")

def multiplicar(x):
    for i in range(1,11):
        print(f"{x} * {i} es igual a {x*i}")

a = int(input("Ingresar un numero a multiplicar: "))

multiplicar(a)
"""

precios=[100,200,55,660,1000]

aumento = lambda x: x+(x*10/100)
nuevalista= list(map(aumento, precios))
print(nuevalista)