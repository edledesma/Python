from src.Services.carServices import *


def menuOptions(root):

    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    car_menu= tk.Menu(my_menu, tearoff="off") #Tearoff removes the cutoff option from menus
    my_menu.add_cascade(label="Car Menu", menu=car_menu)
    car_menu.add_command(label="New Car", command=lambda: newCar(frame))
    car_menu.add_command(label="Delete Car", command=lambda: delCar(frame))
    car_menu.add_command(label="Modify Car", command=lambda: modCar(frame))

    list_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="List Menu", menu=list_menu)
    list_menu.add_command(label="List Car", command=lambda:listCar(frame))
    list_menu.add_command(label="List Cars", command=lambda:listCars(frame))

    frame = tk.LabelFrame(root)
    frame.pack()


