"""
¿Se acercan tus próximas vacaciones en el extranjero y aún no has definido tu presupuesto? Muy bien,
un conversor de monedas puede ser muy útil en estos casos, porque te permitirá conocer el valor de tu moneda en
 otro país y de esta manera puedes prepararte para pasear y comprar el producto que más te guste. ¡Genial!


Escribamos un programa que permita calcular el valor de dólares o euros a:

-Pesos colombianos
-Yuanes
-Libras esterlinas

En esta actividad usaremos un valor promedio para determinar la equivalencia, mire las siguientes tablas:

Dólar (USD)     Equivale a      Moneda
1               3750            pesos colombianos
1               6.37            yuanes
1               0.76            libras esterlinas


Euro (€)        Equivale a      Moneda
1               4000            pesos colombianos
1               6.93            yuanes
1               0.83            libras esterlinas

La función principal tendrá como parámetros:
-El nombre de la moneda actual
-El valor de la moneda actual
-Y el nombre de la moneda a convertir

Y dentro de la función principal estarán dos subfunciones dolarTo() y euroTo(),
las cuales se encargarán de ejecutar las condiciones que permitirán obtener el valor equivalente a la moneda actual.



Nota: Para obtener la equivalencia de una moneda u otra solo basta multiplicar: moneda actual x equivalente.
Por ejemplo, si un dólar es igual a 6.37 yuanes.
¿A cuánto equivale 8 dólares? Simplemente, multiplicamos: 8 x 6.37 = 50.94 yuanes.


"""


def conversor(moneda_act, valor_moneda, moneda_a_convertir):
    if moneda_act == "DOLAR":

        def dolarTO():
            if moneda_a_convertir == "PESOS":
                print(f"${valor_moneda} dolares equivalen a ${valor_moneda*3750} pesos colombianos ")
            elif moneda_a_convertir == "YUANES":
                print(f"${valor_moneda} dolares equivalen a ${valor_moneda * 6.37} yuanes ")
            elif moneda_a_convertir == "LIBRAS":
                print(f"${valor_moneda} dolares equivalen a ${valor_moneda * 0.76} libras ")
            else:
                print("No se puede convertir")
        dolarTO()

    elif moneda_act =="EURO":

        def euroTO():
            if moneda_a_convertir == "PESOS":
                print(f"${valor_moneda} euros equivalen a ${valor_moneda*4000 } pesos colombianos ")
            elif moneda_a_convertir == "YUANES":
                print(f"${valor_moneda} euros equivalen a ${valor_moneda * 6.93 } yuanes ")
            elif moneda_a_convertir == "LIBRAS":
                print(f"${valor_moneda} euros equivalen a ${valor_moneda * 0.83} libras esterlinas ")
            else:
                print("No se puede convertir")
        euroTO()
    else:
        print("Moneda a convertir no valida")

moneda_act = input("Elegir moneda actual:\n - DOLAR\n - EURO  \n")
valor_moneda = float(input("Ingresar el monto de su moneda actual: "))
moneda_a_convertir = input("Ingresar a que moneda desea convertirla:\n - PESOS COLOMBIANOS\n - YUANES\n - LIBRAS ESTERLINAS\n")


conversor(moneda_act, valor_moneda, moneda_a_convertir)

"""
50 DOLARES A PESOS COLOMBIANOS  = 187500
30 EUROS A YUANES               = 207.89999999999998   
15 EUROS A LIBRAS               = 12.45
"""
