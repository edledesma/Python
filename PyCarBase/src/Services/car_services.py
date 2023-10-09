'''
Car services
'''
import tkinter as tk
from src.Dao.car_dao import CarDao

daoC = CarDao()

def clear_frame(frame):
    '''
    Clear the frame of content
    '''
    for widget in frame.winfo_children():
        widget.destroy()

def new_car(frame,root_frame):
    '''
    Add a new car to the DB
    '''
    def submit_all(label_suc):
        model = entry_model.get()
        brand = entry_brand.get()
        year = entry_year.get()
        color = entry_color.get()
        car_obj = (model, brand, year, color)
        daoC.insert_car(car_obj)
        car_info=f"Vehicle {model} added sucessfully"
        label_suc.config(text=car_info)

    print("| 1. Create new car entry")
    clear_frame(frame)
    root_frame.config(text="New car entry")
    label_text = tk.Label(frame, text = "Create new car entry", width=20)
    label_text.grid(row=1,column=0)

    label_model = tk.Label(frame,text= "Input model:")
    label_model.grid(row=2,column=0)
    entry_model = tk.Entry(frame)
    entry_model.grid(row=2,column=1)

    label_brand = tk.Label(frame,text= "Input brand:")
    label_brand.grid(row=3,column=0)
    entry_brand = tk.Entry(frame)
    entry_brand.grid(row=3,column=1)

    label_year = tk.Label(frame,text= "Input year:")
    label_year.grid(row=4,column=0)
    entry_year = tk.Entry(frame)
    entry_year.grid(row=4,column=1)

    label_color = tk.Label(frame,text= "Input color:")
    label_color.grid(row=5,column=0)
    entry_color = tk.Entry(frame)
    entry_color.grid(row=5,column=1)

    label_suc = tk.Label(frame,text = "")
    label_suc.grid(row=7,column=0)

    btn_submit = tk.Button(frame,text= "Submit", command=lambda: submit_all(label_suc))
    btn_submit.grid(row=6,column=0, columnspan = 2)

def list_car(frame,root_frame):
    '''
    Displays all the properties of a single car by ID
    '''

    def get_car(car_id,label_text):
        car = daoC.read_car(car_id)
        car = car[0]
        label_text.config(text=f" ID: {car[0]}\nModel: {car[1]}\nBrand: {car[2]}\nYear: {car[3]}\nColor: {car[4]}")

    print("| 2. List a specific vehicle.")
    clear_frame(frame)
    root_frame.config(text="List a car")
    text_label2 = tk.Label(frame, text = "List a car")
    text_label2.grid(row=1,column=0)

    label_id = tk.Label(frame,text= "Input ID:")
    label_id.grid(row=2,column=0)
    entry_id = tk.Entry(frame)
    entry_id.insert(0,"Enter ID")
    entry_id.grid(row=2,column=1)

    label_text =tk.Label(frame, text = "")
    label_text.grid(row = 4, column = 0, columnspan = 2)

    btn_submit = tk.Button(frame,text= "Submit", command=lambda:get_car(entry_id.get(),label_text))
    btn_submit.grid(row=3,column=0, columnspan = 2)


def list_cars(frame,root_frame):
    '''
    Display list of all cars in the database
    '''
    print("| 3. Display all vehicles.")
    clear_frame(frame)
    root_frame.config(text="All cars in database")
    car_list = daoC.read_cars()
    for car in car_list:
        label_list = tk.Label(frame,text=f" ID: {car[0]} - Model: {car[1]} - Brand: {car[2]} - Year: {car[3]} - Color: {car[4]}")
        label_list.pack(anchor=tk.W)

def del_car(frame,root_frame):
    '''
    Toggles the visisbility to false of a car in the DB
    '''

    def del_car_id(car_id):
        daoC.delete_car(car_id)
        label_text =tk.Label(frame, text = f"Car with ID: {car_id} was deleted")
        label_text.grid(row = 4, column = 0, columnspan = 2)

    print("| 4. Delete a vehicle.")
    clear_frame(frame)
    root_frame.config(text="Delete a car")
    label_id = tk.Label(frame,text= "Input ID:")
    label_id.grid(row=2,column=0)
    entry_id = tk.Entry(frame)
    entry_id.insert(0,"Enter ID")
    entry_id.grid(row=2,column=1)

    btn_submit = tk.Button(frame,text= "Submit", command=lambda:del_car_id(entry_id.get()))
    btn_submit.grid(row=3,column=0, columnspan = 2)


def mod_car(frame,root_frame):
    '''
    Modifies a single paramter of a car in the DB
    '''
    def modify_car(car_id,prop_modify,prop_value,label_text):

        if prop_modify not in ("model","brand","year","color"):
            label_text.config(text="That's not a valid option ")
            print ("OH NO!That's not a valid option")
        else:
            daoC.modify_car(car_id, prop_modify, prop_value)
            car_info= f"Modified {prop_value} {prop_modify} from car ID: {car_id}"
            label_text.config(text=car_info)

    print("| 5. Modify vehicle.")
    clear_frame(frame)
    root_frame.config(text="Modify car entry")
    label_text = tk.Label(frame, text = "Modify car entry")
    label_text.grid(row=1,column=0)

    label_id = tk.Label(frame,text= "Input ID:")
    label_id.grid(row=2,column=0)
    entry_id = tk.Entry(frame)
    entry_id.insert(0,"Enter ID")
    entry_id.grid(row=2,column=1)

    prop_modify = tk.StringVar()
    props = [
        ("Model", "model"),
        ("Brand", "brand"),
        ("Year", "year"),
        ("Color", "color")
    ]
    row = entry_id.grid_info()['row']

    for text, mode in props:
        row += 1
        tk.Radiobutton(frame, text = text, variable = prop_modify, value=mode).grid(row=row, column=0, sticky=tk.W)

    label_text = tk.Label(frame,text="")
    label_text.grid(row = 9, column = 0, columnspan = 2)

    label_value = tk.Label(frame,text= "Input new value:")
    label_value.grid(row=10,column=0)
    entry_value = tk.Entry(frame)
    entry_value.insert(0,"Enter new value")
    entry_value.grid(row=11,column=1)

    btn_submit = tk.Button(frame,text= "Submit", command=lambda:modify_car(entry_id.get(),prop_modify.get(),entry_value.get(),label_text))
    btn_submit.grid(row=12,column=0, columnspan = 2)
