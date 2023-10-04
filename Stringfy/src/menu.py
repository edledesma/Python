"""
Required imports
"""
from tkinter import TclError
from services import (
    tk,
    save_as,
    dark_mode,
    light_mode,
    open_image_dialog,
    open_from_clipboard,
    clear_text,
    copy_all,
)

def menu_gui():
    """
    Create the menu for the tkinter application.
    Returns:
        None
    """
    root = tk.Tk()
    root.title("Stringfy")
    try:
        root.iconbitmap("_internal/icon.ico")
    except TclError:
        pass

    root.geometry("900x500")
    root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
    root.minsize(450, 250)
    menu_elements(root)


def menu_elements(root):
    """
    Create the menu elements for the tkinter application.
    Args:
        root (tk.Tk): The tkinter root window.
    Returns:
        None
    """

    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save as..", command=lambda: save_as(text_display))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    view_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(
        label="Dark mode", command=lambda: dark_mode(root, menu_elements)
    )
    view_menu.add_command(
        label="Light mode", command=lambda: light_mode(root, menu_elements)
    )

    btn_open = tk.Button(
        root, text="Open image", command=lambda: open_image_dialog(text_display, root)
    )
    btn_open.pack(padx=20, pady=5)

    btn_paste = tk.Button(
        root,
        text="Paste clipboard",
        command=lambda: open_from_clipboard(text_display, root),
    )
    btn_paste.pack(padx=20, pady=5)

    frame = tk.LabelFrame(root)
    frame.pack(padx=20, pady=5)

    button_frame = tk.Frame(frame)
    button_frame.pack()

    btn_clear = tk.Button(
        button_frame, text="Clear", command=lambda: clear_text(text_display)
    )
    btn_clear.pack(padx=2, pady=4, ipadx=20, expand=True, fill=tk.BOTH, side=tk.LEFT)

    btn_copy = tk.Button(
        button_frame, text="Copy all", command=lambda: copy_all(text_display, root)
    )
    btn_copy.pack(padx=2, pady=4, ipadx=10, expand=True, fill=tk.BOTH, side=tk.LEFT)

    text_display = tk.Text(frame, height=500, width=300)
    text_display.insert(tk.END, "")
    text_display.pack()

    root.mainloop()
