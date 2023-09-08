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

def open_image_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tif *.tiff")])
    if file_path:
        text = convert_image_to_text(file_path)
        script_path = os.path.dirname(sys.argv[0])  # Get the script's directory
        output_file_path = os.path.join(script_path, "output.txt")
        with open(output_file_path, 'w') as file:
            file.write(text)

app = tk.Tk()
app.title("Image to Text Converter")
app.geometry("300x75") 

button = tk.Button(app, text="Open Image", command=open_image_dialog)
button.pack(padx=20, pady=20)

app.mainloop()