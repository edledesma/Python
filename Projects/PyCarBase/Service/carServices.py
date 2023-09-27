from Entity.Car import Car

Cars = []

def newCar():
    print("Creating new car...")
    model = input("Enter model: ")
    brand = input("Enter brand: ")
    year = input("Enter year: ")
    color = input("Enter color: ")
    idCar = len(Cars)+1
    CarObj= Car(model, brand, year, color,idCar)
    Cars.append(CarObj)

def listCar():
    print("| 2. List a specific vehicle.")
    idCarShow = int(input("Enter vehicle ID :"))-1
    print(f"Model : {Cars[idCarShow].model}\nBrand : {Cars[idCarShow].brand}\nYear : {Cars[idCarShow].year}\nColor : {Cars[idCarShow].color}\nIdCar : {Cars[idCarShow].idCar}")
    input("Press Enter to continue...")
    

def listCars():
    print("| 3. Display all vehicles.")
    for car in Cars:
        print(f"Model : {car.model}\nBrand : {car.brand}\nYear : {car.year}\nColor : {car.color}\nIdCar : {car.idCar}\n___________________________")
    input("Press Enter to continue...")    

def deleteCar():
    print("| 4. Delete a vehicle.")
    idCarDelete = int(input("Enter vehicle ID :"))-1
    print(f"Vehicle {Cars[idCarDelete].model} with ID {Cars[idCarDelete].idCar} was deleted.")
    del Cars[idCarDelete]
    input("Press Enter to continue...")

def modifyCar():
    print("| 5. Modify vehicle.")
    idCarShow = int(input("Enter vehicle ID :"))-1
    propMod = input("Enter the property to modify (Model, Brand, Year, Color): ")
    newValue = input("Enter new value: ")
    Cars[idCarShow].modifyProp(propMod, newValue)
    input("Press Enter to continue...")