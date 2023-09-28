import sqlite3

class carDAO:
    def __init__(self):
        self.con = sqlite3.connect('cars.db')
        self.cur = self.con.cursor()
        self.createCarTable()
    
    def createCarTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, brand TEXT, year INTEGER, color TEXT)''')
        self.con.commit()

    def insertCar(self, item):
        self.cur.execute('''INSERT INTO cars(model, brand, year, color) VALUES(?,?,?,?)''', item)
        self.con.commit()

    def readCar(self,carId):
        self.cur.execute('''SELECT *FROM cars WHERE id = ?''' ,carId)
        rows = self.cur.fetchall()
        return rows   

    def readCars(self):
        self.cur.execute('''SELECT *FROM cars''')
        rows = self.cur.fetchall()
        return rows