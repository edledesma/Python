from src.Services.menuServices import *
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
import sqlite3

# app = QApplication(sys.argv)

# window = QMainWindow()
# window.setWindowTitle("PyCarBase")

# window.show()
# app.exec()



while True:
    if menuOp() == "quit":
        print("Goodbye")
        break