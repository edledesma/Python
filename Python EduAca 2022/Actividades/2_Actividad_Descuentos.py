"""
Imagine que la tienda donde usted trabaja ofrece descuentos a los clientes en navidad, de acuerdo con el monto de su compra.
El criterio para establecer el descuento se muestra a continuación:


Compra (USD)                                        Porcentaje

Sí es menor a 80                                    0%
Sí es mayor o igual a 80 y menor que 150            10%
Sí es mayor o igual a 150 y menor o igual a 300     15%
Sí es mayor a 300 y menor a 500                     20%


Teniendo en cuenta la tabla, te piden que escribas un programa que solicite el nombre del cliente y el valor de la compra.
 Y que arroje como resultado:
 -Nombre del cliente
 -Valor de la compra sin descuento
 -Valor de la compra con descuento


Recuerde que para calcular el descuento primero debe multiplicar el valor de la compra por el porcentaje.
Luego, debe restar el valor obtenido al valor de la compra y con eso obtiene el precio con descuento.
-  descuento = valor_compra x porcentaje
-   precio final = valor_compra - descuento

"""
cliente = input("Ingresar apellido del usario: ")
compra = float(input("Ingresar total de compra: "))

if compra < 80:
    descuento = 0
elif compra >= 80 and compra < 150:
    descuento = 0.1
elif compra >= 150 and compra <= 300:
    descuento = 0.15
elif compra > 300 and compra < 500:
    descuento = 0.2
else:
    descuento = 0.2

precio_final = compra -( compra * descuento)

print(f"{cliente} el valor de su compra es ${compra} \nCon su descuento, el valor final es ${precio_final}")

"""
¿Cuál es el valor de las siguientes compras con descuento? 
Angel Mario Villa Lopez -   Sin descuento: $455 - Con Descuento: $364.0
Rosa Diaz -                 Sin descuento: $105 - Con Descuento: $94.5
Dilan Gonzalez -            Sin descuento: $250 - Con Descuento: $212.5
Kelly Daza -                Sin descuento: $430 - Con Descuento: $$344.0
"""