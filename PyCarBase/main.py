from src.Services.menuServices import *

root = tk.Tk()
root.title("CarBase")
try:
    root.iconbitmap('src\Media\hatch.ico')
except Exception:
    pass
root.geometry("600x400")
menuOptions(root)

root.mainloop()

