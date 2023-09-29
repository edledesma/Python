from src.DAO.carDAO import carDAO
import tkinter as tk

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
    aLabel = tk.Label(frame, text = "Create new car entry", width=20)
    aLabel.grid(row=1,column=0)
    
    LabelModel = tk.Label(frame,text= "Input model:")
    LabelModel.grid(row=2,column=0, sticky=tk.E)
    entryModel = tk.Entry(frame)
    entryModel.insert(0,"Enter model")
    entryModel.grid(row=2,column=1)

    Labelbrand = tk.Label(frame,text= "Input brand:")
    Labelbrand.grid(row=3,column=0)
    entrybrand = tk.Entry(frame)
    entrybrand.grid(row=3,column=1)

    LabelYear = tk.Label(frame,text= "Input year:")
    LabelYear.grid(row=4,column=0)
    entryYear = tk.Entry(frame)
    entryYear.grid(row=4,column=1)


    LabelColor = tk.Label(frame,text= "Input color:")
    LabelColor.grid(row=5,column=0)
    entryColor = tk.Entry(frame)
    entryColor.grid(row=5,column=1)

    LabelSuc = tk.Label(frame,text = "")
    LabelSuc.grid(row=7,column=0)
    
    btnSubmit = tk.Button(frame,text= "Submit", command=lambda: submitAll(LabelSuc))
    btnSubmit.grid(row=6,column=0, columnspan = 2)
    

def listCar(frame):

    def getCar(carid,aLabel):
        car = daoC.readCar(carid)
        car = car[0]
        aLabel.config(text=f" ID: {car[0]}\nModel: {car[1]}\nBrand: {car[2]}\nYear: {car[3]}\nColor: {car[4]}")
        
    
    print("| 2. List a specific vehicle.")
    clearFrame(frame)
    bLabel = tk.Label(frame, text = "List a car")
    bLabel.grid(row=1,column=0)

    LabelID = tk.Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = tk.Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)

    aLabel =tk.Label(frame, text = "")
    aLabel.grid(row = 4, column = 0, columnspan = 2)

    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:getCar(entryID.get(),aLabel))
    btnSubmit.grid(row=3,column=0, columnspan = 2)


def listCars(frame):
    print("| 3. Display all vehicles.")
    clearFrame(frame)
    carList = daoC.readCars()
    for car in carList:
        labelList = tk.Label(frame,text=f" ID: {car[0]} - Model: {car[1]} - Brand: {car[2]} - Year: {car[3]} - Color: {car[4]}")
        labelList.pack(anchor=tk.W)
    
def delCar(frame):

    def delCarId(carId):
        daoC.deleteCar(carId)
        aLabel =tk.Label(frame, text = f"Car with ID: {carId} was deleted")
        aLabel.grid(row = 4, column = 0, columnspan = 2)

    print("| 4. Delete a vehicle.")
    clearFrame(frame)

    LabelID = tk.Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = tk.Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)
    
    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:delCarId(entryID.get()))
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
    aLabel = tk.Label(frame, text = "Modify car entry")
    aLabel.grid(row=1,column=0)

    LabelID = tk.Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = tk.Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)
    
    propModify = tk.StringVar()
    Props = [
        ("Model", "model"),
        ("Brand", "brand"),
        ("Year", "year"),
        ("Color", "color")
    ]
    row = entryID.grid_info()['row'] 

    for text, mode in Props:
        row += 1
        tk.Radiobutton(frame, text = text, variable = propModify, value=mode).grid(row=row, column=0, sticky=tk.W)

    aLabel = tk.Label(frame,text="")
    aLabel.grid(row = 9, column = 0, columnspan = 2)    

    LabelValue = tk.Label(frame,text= "Input new value:")
    LabelValue.grid(row=10,column=0)
    entryValue = tk.Entry(frame)
    entryValue.insert(0,"Enter new value")
    entryValue.grid(row=11,column=1)

    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:modifyCar(entryID.get(),propModify.get(),entryValue.get(),aLabel))
    btnSubmit.grid(row=12,column=0, columnspan = 2)
