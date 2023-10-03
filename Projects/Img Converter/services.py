from tkinter import filedialog
from PIL import Image,ImageGrab
import tkinter as tk
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path to your Tesseract installation, this is the default by Tesseract OCR

def save_as(textDisplay):
    text = textDisplay.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(initialfile='converted.txt',filetypes=[("Text files", "*.txt")])
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    with open(file_path, 'w') as file:
        file.write(text)

def dark_mode(root,menu):
    root.tk_setPalette(background='#525252', foreground='#ffffff')
    for widget in root.winfo_children():
        widget.destroy()
    menu(root)

def light_mode(root,menu):
    root.tk_setPalette(background='SystemButtonFace', foreground='SystemWindowText')
    root.option_clear()
    for widget in root.winfo_children():
        widget.destroy()
    menu(root)

def convert_image_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def clear_text(textDisplay):
    textDisplay.delete(1.0, tk.END)

def copy_all(textDisplay,root):
    root.clipboard_clear()
    root.clipboard_append(textDisplay.get(1.0, tk.END))

def open_from_clipboard(textDisplay,root):
    clear_text(textDisplay)
    try:
        text = pytesseract.image_to_string(ImageGrab.grabclipboard() )  
        updateText(textDisplay,root, text)
    except:
        updateText(textDisplay,root,"No image in paperclip")

def open_image_dialog(textDisplay,root):
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tif *.tiff")])
        if file_path:
            clear_text(textDisplay)
            text = convert_image_to_text(file_path)
        updateText(textDisplay, root,text)
    except:
        pass

def updateText(textDisplay,root,text):
    textDisplay.insert(tk.END,text)
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Copy", command=lambda: root.clipboard_clear() or root.clipboard_append(textDisplay.get("sel.first", "sel.last")))
    context_menu.add_separator()
    context_menu.add_command(label="Cut", command=lambda: root.clipboard_clear() or root.clipboard_append(textDisplay.get("sel.first", "sel.last")) or textDisplay.delete("sel.first", "sel.last"))
    context_menu.add_separator()
    context_menu.add_command(label="Paste", command=lambda: textDisplay.insert(tk.INSERT, root.clipboard_get()))
    textDisplay.bind("<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root))
