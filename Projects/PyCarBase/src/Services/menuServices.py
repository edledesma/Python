import os
from src.Services.carServices import *

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuOp():
    print(" ")
    print("|---Welcome to CarBase!----|")
    print("|__________________________|")
    print("|Choose what you want to do|")
    print("|__________________________|")
    print("| 1. Enter a new vehicle.")
    print("| 2. List a specific vehicle.")
    print("| 3. Display all vehicles.")
    print("| 4. Delete a vehicle.")
    print("| 5. Modify a vehicle.")
    print("| 6. EXIT.")
    print("                       ")
    print("Type your choice")
    while True:
        choice = ""
        if type(choice) == int:
            break
        else:
            try:
                choice = int(input("> "))
            except:
                clear_console()
                print("Invalid input. Try again.")
        break
    match (choice):
        case 1:
            clear_console()
            newCar()
        case 2:
            clear_console()
            listCar()
        case 3:
            clear_console()
            listCars()
        case 4:
            clear_console()
            deleteCar()
        case 5:
            clear_console()
            modifyCar()
        case 6:
            clear_console()
            return "quit"
    
