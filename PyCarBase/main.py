'''
Main function
'''
import tkinter as tk
from src.Services.menu_services import menu_options

root = tk.Tk()
root.title("CarBase")
try:
    root.iconbitmap('src/Media/hatch.ico')
except tk.TclError as e:
    pass
root.geometry("600x400")
menu_options(root)

root.mainloop()
