from src.Services.carServices import *
from tkinter import *

def menuOptions(root):

    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Exit", command=root.quit)

    car_menu= Menu(my_menu)
    my_menu.add_cascade(label="Car Menu", menu=car_menu)
    car_menu.add_command(label="New Car", command=lambda: newCar(frame))
    car_menu.add_command(label="Delete Car", command=lambda: delCar(frame))
    car_menu.add_command(label="Modify Car", command=lambda: modCar(frame))

    list_menu = Menu(my_menu)
    my_menu.add_cascade(label="List Menu", menu=list_menu)
    list_menu.add_command(label="List Car", command=lambda:listCar(frame))
    list_menu.add_command(label="List Cars", command=lambda:listCars(frame))

    frame = LabelFrame(root)
    frame.grid(row=1, column=0)


