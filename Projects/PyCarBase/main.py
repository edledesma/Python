from src.Services.menuServices import *
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_directory, "src\Media", "icon.ico")

root = Tk()

root.title("CarBase")

root.iconbitmap(icon_path)
root.geometry("600x400")
menuOptions(root)

root.mainloop()

