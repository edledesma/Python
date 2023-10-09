'''
Menu services
'''
import tkinter as tk
from src.Services.car_services import new_car, del_car, mod_car, list_car, list_cars


def menu_options(root):
    '''
    Menu displays options
    '''

    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    car_menu= tk.Menu(my_menu, tearoff="off") #Tearoff removes the cutoff option from menus
    my_menu.add_cascade(label="Car Menu", menu=car_menu)
    car_menu.add_command(label="New Car", command=lambda: new_car(frame,root_frame))
    car_menu.add_command(label="Delete Car", command=lambda: del_car (frame,root_frame))
    car_menu.add_command(label="Modify Car", command=lambda: mod_car (frame,root_frame))

    list_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="List Menu", menu=list_menu)
    list_menu.add_command(label="List Car", command=lambda:list_car (frame,root_frame))
    list_menu.add_command(label="List Cars", command=lambda:list_cars (frame,root_frame))

    root_frame = tk.Label(root, text="Welcome to CarBase")
    root_frame.pack(pady=10,fill=tk.X)
    frame = tk.LabelFrame(root)
    frame.pack(pady=20)
