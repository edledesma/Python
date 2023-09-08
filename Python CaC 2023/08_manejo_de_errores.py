while True:
    try:
        n = float(input("Ingresar un numero: "))
        m= 4.0
        print(f"{n}/{m} = {n/m}")
    except:
        print("Error. \nIntroduzca un numero") 
    else:
        print(f"Se ingreso el número {n}")
        break
    finally:
        print("--Finalizado el intento")