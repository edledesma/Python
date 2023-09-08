"""
El ciclo While revisa la condición dada, si es verdadera ejecuta las instrucciones y luego vuelve a revisar la condición
Este proceso se repite hasta que la condición sea falsa.
GUARDA CON LOS BUCLES INFINITOS

while condition:
    cuerpo del bucle
"""

# Calculadora de BMI - Ejemplo

contador = 0

print("CALCULADORA DE BMI \n")

while contador != 2:
    contador = int(input("¿Quieres seguir calculando el BMI? 1.SI y 2.NO \n"))

    if contador == 1:
        estatura = float(input("¿Cual es tu estatura en mts?: "))
        peso = float(input("¿Cual es tu peso en kgs?: "))
        resultado = round(peso/(estatura **2) ,2)

        if resultado < 18.5:
            print(f"BMI {resultado} = BAJO DE PESO")
        elif 18.5 < resultado < 24.99:
            print(f"BMI {resultado} = PESO NORMAL")
        elif 25 < resultado < 30:
            print(f"BMI {resultado} = SOBREPESO")
        elif resultado > 30:
            print(f"BMI {resultado} = OBESIDAD")
    elif contador == 2:
        print("Hasta pronto")
print("Gracias por calcular el BMI")