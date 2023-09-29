from src.Entities.Car import Car
from src.DAO.carDAO import carDAO

daoC = carDAO()

def newCar():
    print("Creating new car...")
    model = input("Enter model: ")
    brand = input("Enter brand: ")
    year = input("Enter year: ")
    color = input("Enter color: ")
    CarObj = (model, brand, year, color)
    daoC.insertCar(CarObj)
    
def listCar():
    print("| 2. List a specific vehicle.")
    carId = input("Enter CAR ID: ")
    print(daoC.readCar(carId))
    input("Press enter to continue...")


def listCars():
    print("| 3. Display all vehicles.")
    print(daoC.readCars())
    input("Press enter to continue...")
    

def deleteCar():
    print("| 4. Delete a vehicle.")
    carId = input("Enter CAR ID: ")
    daoC.deleteCar(carId)
    input("Press Enter to continue...")

def modifyCar():
    print("| 5. Modify vehicle.")
    carID = input("Enter CAR ID: ")
    propModify = input("What value do you wish to modify? (Model, Brand, Year, color): ")
    propValue = input ("Input new value: ")
    print(daoC.modifyCar(carID, propModify, propValue))
    input("Press enter to continue...")
  