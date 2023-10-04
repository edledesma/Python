from services import *

def menu(root):

    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Save as..", command=lambda:save_as(textDisplay))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    view_menu = tk.Menu(my_menu, tearoff="off")
    my_menu.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Dark mode", command=lambda:dark_mode(root,menu))
    view_menu.add_command(label="Light mode", command=lambda:light_mode(root,menu))

    btnOpen = tk.Button(root, text="Open image", command=lambda:open_image_dialog(textDisplay,root))
    btnOpen.pack(padx=20, pady=5)

    btnPaste = tk.Button(root, text="Paste clipboard", command=lambda:open_from_clipboard(textDisplay,root))
    btnPaste.pack(padx=20, pady=5)

    frame = tk.LabelFrame(root)
    frame.pack(padx=20, pady=5)

    buttonFrame = tk.Frame(frame)
    buttonFrame.pack()

    btnClear = tk.Button(buttonFrame, text="Clear", command=lambda:clear_text(textDisplay))
    btnClear.pack(padx=2,pady=4,ipadx=20,expand=True, fill=tk.BOTH, side=tk.LEFT)

    btnCopy = tk.Button(buttonFrame, text="Copy all", command=lambda:copy_all(textDisplay,root) )
    btnCopy.pack(padx=2,pady=4,ipadx=10,expand=True, fill=tk.BOTH, side=tk.LEFT)

    textDisplay = tk.Text(frame, height=500, width=300)
    textDisplay.insert(tk.END,"")
    textDisplay.pack()

