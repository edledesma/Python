import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image
import os
import sys

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path to your Tesseract installation

def convert_image_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def clear_text(textDisplay):
    textDisplay.delete(1.0, tk.END)

def open_image_dialog(textDisplay):
    
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tif *.tiff")])
    if file_path:
        textDisplay.delete(1.0, tk.END)
        text = convert_image_to_text(file_path)
        thistext = text
        textDisplay.insert(tk.END,thistext)

        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Copy", command=lambda: root.clipboard_clear() or root.clipboard_append(textDisplay.get("sel.first", "sel.last")))
        context_menu.add_separator()
        context_menu.add_command(label="Cut", command=lambda: root.clipboard_clear() or root.clipboard_append(textDisplay.get("sel.first", "sel.last")) or textDisplay.delete("sel.first", "sel.last"))
        context_menu.add_separator()
        context_menu.add_command(label="Paste", command=lambda: textDisplay.insert(tk.INSERT, root.clipboard_get()))

        textDisplay.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))

root = tk.Tk()
root.title("Img2Text")
try:
    root.iconbitmap('icon.ico')
except Exception:
    pass

root.geometry("900x500") 

button = tk.Button(root, text="Open Image", command=lambda:open_image_dialog(textDisplay))
button.pack(padx=20, pady=10)

button = tk.Button(root, text="Clear", command=lambda:clear_text(textDisplay))
button.pack(padx=1, pady=1)

frame = tk.LabelFrame(root)
frame.pack(padx=20, pady=5)

textDisplay = tk.Text(frame, height=500, width=300)
textDisplay.insert(tk.END,"")
textDisplay.pack()

label = tk.Label(frame, text="Text")
label.pack(padx=20, pady=5)





root.mainloop()