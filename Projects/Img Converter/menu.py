import tkinter as tk
from tkinter import filedialog
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path to your Tesseract installation, this is the default by Tesseract OCR


def menu(root):

    def save_as():
        text = textDisplay.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(initialfile='converted.txt',filetypes=[("Text files", "*.txt")])
        if not file_path.endswith(".txt"):
            file_path += ".txt"
        with open(file_path, 'w') as file:
            file.write(text)

    def dark_mode():
        root.tk_setPalette(background='#525252', foreground='#ffffff')
        for widget in root.winfo_children():
            widget.destroy()
        menu(root)

    def light_mode():
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

    def copy_all(textDisplay):
        root.clipboard_clear()
        root.clipboard_append(textDisplay.get(1.0, tk.END))

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

    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save as..", command=save_as)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    view_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Dark Mode", command=dark_mode)
    view_menu.add_command(label="Light Mode", command=light_mode)

    button = tk.Button(root, text="Open Image", command=lambda:open_image_dialog(textDisplay))
    button.pack(padx=20, pady=5)

    frame = tk.LabelFrame(root)
    frame.pack(padx=20, pady=5)

    buttonFrame = tk.Frame(frame)
    buttonFrame.pack()

    aButton = tk.Button(buttonFrame, text="Clear", command=lambda:clear_text(textDisplay))
    aButton.pack(padx=2,pady=4,ipadx=20,expand=True, fill=tk.BOTH, side=tk.LEFT)

    bButton = tk.Button(buttonFrame, text="Copy all", command=lambda:copy_all(textDisplay) )
    bButton.pack(padx=2,pady=4,ipadx=10,expand=True, fill=tk.BOTH, side=tk.LEFT)

    textDisplay = tk.Text(frame, height=500, width=300)
    textDisplay.insert(tk.END,"")
    textDisplay.pack()

