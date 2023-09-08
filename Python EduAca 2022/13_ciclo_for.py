# Ejemplo 3

# Vamos a crear una tabla de multiplicar

numero = int(input("¿De que numero quieres la tabla de multiplicar?: "))
print("")

print(f"Tabla de multiplicar del numero {numero}")
for i in range(1, 11):
    print(f" {i} x {numero} = {i*numero}")
