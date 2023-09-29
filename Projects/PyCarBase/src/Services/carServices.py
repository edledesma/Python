from src.DAO.carDAO import carDAO
import tkinter as tk

daoC = carDAO()

def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def newCar(frame,rootFrame):
        
    def submitAll(labelSuc):
        model = entryModel.get()
        brand = entryBrand.get()
        year = entryYear.get()
        color = entryColor.get()
        CarObj = (model, brand, year, color)
        daoC.insertCar(CarObj)
        car_Info= (f"Vehicle {model} added sucessfully")
        labelSuc.config(text=car_Info)
        
    print("| 1. Create new car entry")    
    clearFrame(frame)
    rootFrame.config(text="New car entry")
    aLabel = tk.Label(frame, text = "Create new car entry", width=20)
    aLabel.grid(row=1,column=0)
    
    labelModel = tk.Label(frame,text= "Input model:")
    labelModel.grid(row=2,column=0)
    entryModel = tk.Entry(frame)
    entryModel.grid(row=2,column=1)

    labelBrand = tk.Label(frame,text= "Input brand:")
    labelBrand.grid(row=3,column=0)
    entryBrand = tk.Entry(frame)
    entryBrand.grid(row=3,column=1)

    labelYear = tk.Label(frame,text= "Input year:")
    labelYear.grid(row=4,column=0)
    entryYear = tk.Entry(frame)
    entryYear.grid(row=4,column=1)


    labelColor = tk.Label(frame,text= "Input color:")
    labelColor.grid(row=5,column=0)
    entryColor = tk.Entry(frame)
    entryColor.grid(row=5,column=1)

    labelSuc = tk.Label(frame,text = "")
    labelSuc.grid(row=7,column=0)
    
    btnSubmit = tk.Button(frame,text= "Submit", command=lambda: submitAll(labelSuc))
    btnSubmit.grid(row=6,column=0, columnspan = 2)
    

def listCar(frame,rootFrame):

    def getCar(carid,aLabel):
        car = daoC.readCar(carid)
        car = car[0]
        aLabel.config(text=f" ID: {car[0]}\nModel: {car[1]}\nBrand: {car[2]}\nYear: {car[3]}\nColor: {car[4]}")
        
    
    print("| 2. List a specific vehicle.")
    clearFrame(frame)
    rootFrame.config(text="List a car")
    bLabel = tk.Label(frame, text = "List a car")
    bLabel.grid(row=1,column=0)

    labelID = tk.Label(frame,text= "Input ID:")
    labelID.grid(row=2,column=0)
    entryID = tk.Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)

    aLabel =tk.Label(frame, text = "")
    aLabel.grid(row = 4, column = 0, columnspan = 2)

    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:getCar(entryID.get(),aLabel))
    btnSubmit.grid(row=3,column=0, columnspan = 2)


def listCars(frame,rootFrame):
    print("| 3. Display all vehicles.")
    clearFrame(frame)
    rootFrame.config(text="All cars in database")
    carList = daoC.readCars()
    for car in carList:
        labelList = tk.Label(frame,text=f" ID: {car[0]} - Model: {car[1]} - Brand: {car[2]} - Year: {car[3]} - Color: {car[4]}")
        labelList.pack(anchor=tk.W)
    
def delCar(frame,rootFrame):

    def delCarId(carID):
        daoC.deleteCar(carID)
        aLabel =tk.Label(frame, text = f"Car with ID: {carID} was deleted")
        aLabel.grid(row = 4, column = 0, columnspan = 2)

    print("| 4. Delete a vehicle.")
    clearFrame(frame)
    rootFrame.config(text="Delete a car")
    LabelID = tk.Label(frame,text= "Input ID:")
    LabelID.grid(row=2,column=0)
    entryID = tk.Entry(frame)
    entryID.insert(0,"Enter ID")
    entryID.grid(row=2,column=1)
    
    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:delCarId(entryID.get()))
    btnSubmit.grid(row=3,column=0, columnspan = 2)


def modCar(frame,rootFrame):
    
    def modifyCar(carID,propModify,propValue,aLabel):
        
        if propModify != "model" and propModify != "brand" and propModify != "year" and propModify != "color":
            aLabel.config(text="That's not a valid option ")
            print ("OH NO!That's not a valid option")
        else:
            daoC.modifyCar(carID, propModify, propValue)
            car_Info= (f"Modified {propValue} {propModify} from car ID: {carID}")
            aLabel.config(text=car_Info)
            

    print("| 5. Modify vehicle.")
    clearFrame(frame)
    rootFrame.config(text="Modify car entry")
    aLabel = tk.Label(frame, text = "Modify car entry")
    aLabel.grid(row=1,column=0)

    labelID = tk.Label(frame,text= "Input ID:")
    labelID.grid(row=2,column=0)
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

    labelValue = tk.Label(frame,text= "Input new value:")
    labelValue.grid(row=10,column=0)
    entryValue = tk.Entry(frame)
    entryValue.insert(0,"Enter new value")
    entryValue.grid(row=11,column=1)

    btnSubmit = tk.Button(frame,text= "Submit", command=lambda:modifyCar(entryID.get(),propModify.get(),entryValue.get(),aLabel))
    btnSubmit.grid(row=12,column=0, columnspan = 2)
