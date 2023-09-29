from src.DAO.carDAO import carDAO
from tkinter import *

daoC = carDAO()

def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def newCar(frame):
        
    def submitAll(LabelSuc):
        model = entryModel.get()
        brand = entrybrand.get()
        year = entryYear.get()
        color = entryColor.get()
        CarObj = (model, brand, year, color)
        daoC.insertCar(CarObj)
        car_Info= (f"Vehicle {model} added sucessfully")
        LabelSuc.config(text=car_Info)
        
    print("| 1. Create new car entry")    
    clearFrame(frame)
    aLabel = Label(frame, text = "Create new car entry")
    aLabel.grid(row=1,column=0)
    
    LabelModel = Label(frame,text= "Input model:")
    LabelModel.grid(row=2,column=0)
    entryModel = Entry(frame)
    entryModel.insert(0,"Enter model")
    entryModel.grid(row=2,column=1)

    Labelbrand = Label(frame,text= "Input brand:")
    Labelbrand.grid(row=3,column=0)
    entrybrand = Entry(frame)
    entrybrand.grid(row=3,column=1)

    LabelYear = Label(frame,text= "Input year:")
    LabelYear.grid(row=4,column=0)
    entryYear = Entry(frame)
    entryYear.grid(row=4,column=1)


    LabelColor = Label(frame,text= "Input color:")
    LabelColor.grid(row=5,column=0)
    entryColor = Entry(frame)
    entryColor.grid(row=5,column=1)

    LabelSuc = Label(frame,text = "")
    LabelSuc.grid(row=7,column=0)
    
    btnSubmit = Button(frame,text= "Submit", command=lambda: submitAll(LabelSuc))
    btnSubmit.grid(row=6,column=0, columnspan = 2)
    

def listCar(frame):

    def getCar(carid,aLabel):
        car_info = daoC.readCar(carid)
        aLabel.config(text=car_info)
        
    
    print("| 2. List a specific vehicle.")
    clearFrame(frame)
    bLabel = Label(frame, text = "List a car")
    bLabel.grid(row=1,column=0)

    LabelID = Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)

    aLabel =Label(frame, text = "")
    aLabel.grid(row = 4, column = 0, columnspan = 2)

    btnSubmit = Button(frame,text= "Submit", command=lambda:getCar(entryID.get(),aLabel))
    btnSubmit.grid(row=3,column=0, columnspan = 2)


def listCars(frame):
    print("| 3. Display all vehicles.")
    clearFrame(frame)
    bLabel = Label(frame, text = daoC.readCars())
    bLabel.grid(row=1,column=0)
    
    

def delCar(frame):

    def delCarId(carId):
        daoC.deleteCar(carId)
        aLabel =Label(frame, text = f"Car with ID: {carId} was deleted")
        aLabel.grid(row = 4, column = 0, columnspan = 2)

    print("| 4. Delete a vehicle.")
    clearFrame(frame)

    LabelID = Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)
    
    btnSubmit = Button(frame,text= "Submit", command=lambda:delCarId(entryID.get()))
    btnSubmit.grid(row=3,column=0, columnspan = 2)


def modCar(frame):
    
    def modifyCar(carId,propModify,propValue,aLabel):
        
        if propModify != "model" and propModify != "brand" and propModify != "year" and propModify != "color":
            aLabel.config(text="That's not a valid option ")
            print ("OH NO!That's not a valid option")
        else:
            daoC.modifyCar(carId, propModify, propValue)
            car_Info= (f"Modiying {propValue} {propModify} from car ID: {carId}")
            aLabel.config(text=car_Info)
            

    print("| 5. Modify vehicle.")
    clearFrame(frame)
    aLabel = Label(frame, text = "Modify car entry")
    aLabel.grid(row=1,column=0)

    LabelID = Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)
    
    propModify = StringVar()
    Props = [
        ("Model", "model"),
        ("Brand", "brand"),
        ("Year", "year"),
        ("Color", "color")
    ]
    row = entryID.grid_info()['row'] 

    for text, mode in Props:
        row += 1
        Radiobutton(frame, text = text, variable = propModify, value=mode).grid(row=row, column=0, sticky=W)

    aLabel = Label(frame,text="")
    aLabel.grid(row = 9, column = 0, columnspan = 2)    

    LabelValue = Label(frame,text= "Input new value:")
    LabelValue.grid(row=10,column=0)
    entryValue = Entry(frame)
    entryValue.insert(0,"Enter new value")
    entryValue.grid(row=11,column=1)

    btnSubmit = Button(frame,text= "Submit", command=lambda:modifyCar(entryID.get(),propModify.get(),entryValue.get(),aLabel))
    btnSubmit.grid(row=12,column=0, columnspan = 2)
