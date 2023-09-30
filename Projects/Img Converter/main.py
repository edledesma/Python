from menu import *

root = tk.Tk()
root.title("Img2Text")
try:
    root.iconbitmap('icon.ico')
except Exception:
    pass

root.geometry("900x500") 
root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.minsize(450,250)
menu(root)
root.mainloop()