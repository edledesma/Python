"""
Required imports
"""
import os
import sys
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageGrab, UnidentifiedImageError
import pytesseract
from pytesseract import TesseractError

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
if not os.path.exists(TESSERACT_PATH):
    while True:
        TESSERACT_PATH = filedialog.askopenfilename(title="Select Tesseract Executable",
                                                    filetypes=[("Executable files", "*.exe")])
        if not TESSERACT_PATH:
            sys.exit()
        if os.path.basename(TESSERACT_PATH) != "tesseract.exe":
            print("Invalid selection. Please choose the Tesseract executable (tesseract.exe).")
        else:
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
            print("Tesseract executable selected:", TESSERACT_PATH)
            break

def save_as(text_display):
    """
    Save the contents of the text_display to a file.
    Args:
        text_display (tk.Text): The tkinter Text widget containing the text to be saved.
    Returns:
        None
    """
    text = text_display.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(
        initialfile="converted.txt", filetypes=[("Text files", "*.txt")]
    )
    if not file_path.endswith(".txt"):
        file_path += ".txt"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def dark_mode(root, menu_elements):
    """
    Set the dark mode theme for the tkinter application.
    Args:
        root (tk.Tk): The tkinter root window.
        menu (function): The menu function to be called after setting the dark mode theme.
    Returns:
        None
    """
    root.tk_setPalette(background="#525252", foreground="#ffffff")
    for widget in root.winfo_children():
        widget.destroy()
    menu_elements(root)


def light_mode(root, menu_elements):
    """
    Set the light mode theme for the tkinter application.
    Args:
        root (tk.Tk): The tkinter root window.
        menu (function): The menu function to be called after setting the light mode theme.
    Returns:
        None
    """
    root.tk_setPalette(background="SystemButtonFace", foreground="SystemWindowText")
    root.option_clear()
    for widget in root.winfo_children():
        widget.destroy()
    menu_elements(root)


def convert_image_to_text(image_path):
    """
    Convert an image to text using Tesseract OCR.
    Args:
        image_path (str): The file path to the input image.

    Returns:
        str: The extracted text from the image.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except pytesseract.pytesseract.TesseractNotFoundError:
        return "Error: Tesseract OCR couldn't process the image. "


def clear_text(text_display):
    """
    Clear the text displayed in the tkinter Text widget.
    Args:
        text_display (tk.Text): The tkinter Text widget to be cleared.
    Returns:
        None
    """
    text_display.delete(1.0, tk.END)


def copy_all(text_display, root):
    """
    Copy all text from the tkinter Text widget to the clipboard.
    Args:
        text_display (tk.Text): The tkinter Text widget containing the text to be copied.
        root (tk.Tk): The tkinter root window.
    Returns:
        None
    """
    root.clipboard_clear()
    root.clipboard_append(text_display.get(1.0, tk.END))


def open_from_clipboard(text_display, root):
    """
    Open an image from the clipboard and extract text using Tesseract OCR.
    Args:
        text_display (tk.Text): The tkinter Text widget to display the extracted text.
        root (tk.Tk): The tkinter root window.
    Returns:
        None
    """
    clear_text(text_display)
    try:
        clipboard_image = ImageGrab.grabclipboard()
        if clipboard_image is not None:
            text = pytesseract.image_to_string(clipboard_image)
            update_text(text_display, root, text)
        else:
            update_text(text_display, root, "No image in clipboard")
    except AttributeError:
        update_text(text_display, root, "Error: Unable to access clipboard or image")
    except TesseractError:
        update_text(
            text_display, root, "Error: Tesseract OCR failed to process the image"
        )


def open_image_dialog(text_display, root):
    """
    Open a file dialog to select an image file, extract text 
    from the image, and display it in the tkinter Text widget.
    Args:
        text_display (tk.Text): The tkinter Text widget to display the extracted text.
        root (tk.Tk): The tkinter root window.
    Returns:
        None
    """
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tif *.tiff")]
        )
        if file_path:
            clear_text(text_display)
            text = convert_image_to_text(file_path)
        update_text(text_display, root, text)
    except UnidentifiedImageError:
        update_text(text_display, root, "Error: Unable to identify image")

def update_text(text_display, root, text):
    """
    Update the text displayed in the tkinter Text widget and bind a context menu to it.
    Args:
        text_display (tk.Text): The tkinter Text widget to display the text.
        root (tk.Tk): The tkinter root window.
        text (str): The text to be displayed in the Text widget.
    Returns:
        None
    """
    text_display.insert(tk.END, text)
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(
        label="Copy",
        command=lambda: root.clipboard_clear()
        or root.clipboard_append(text_display.get("sel.first", "sel.last")),
    )
    context_menu.add_separator()
    context_menu.add_command(
        label="Cut",
        command=lambda: root.clipboard_clear()
        or root.clipboard_append(text_display.get("sel.first", "sel.last"))
        or text_display.delete("sel.first", "sel.last"),
    )
    context_menu.add_separator()
    context_menu.add_command(
        label="Paste",
        command=lambda: text_display.insert(tk.INSERT, root.clipboard_get()),
    )
    text_display.bind(
        "<Button-3>", lambda event: context_menu.post(event.x_root, event.y_root)
    )
