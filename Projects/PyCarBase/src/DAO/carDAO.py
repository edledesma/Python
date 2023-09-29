import sqlite3

class carDAO:
    def __init__(self):
        self.con = sqlite3.connect('cars.db')
        self.cur = self.con.cursor()
        self.createCarTable()
    
    def createCarTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, brand TEXT, year INTEGER, color TEXT, isActive TEXT DEFAULT 'True')''')
        self.con.commit()

    def insertCar(self, item):
        self.cur.execute('''INSERT INTO cars(model, brand, year, color) VALUES(?,?,?,?)''', item)
        self.con.commit()

    def readCar(self,carId):
        self.cur.execute('''SELECT *FROM cars WHERE id = ?''' ,carId)
        rows = self.cur.fetchall()
        return rows   

    def readCars(self):
        self.cur.execute('''SELECT *FROM cars WHERE isActive = 'True' ''')
        rows = self.cur.fetchall()
        return rows
    
    def deleteCar(self,carId):
        self.cur.execute('''UPDATE cars SET isActive = 'False' WHERE id = ? ''',carId)
        self.con.commit()
    
    def modifyCar(self,carId,propModify, propValue):
        self.cur.execute(f'''UPDATE cars SET  {propModify} = ? WHERE id = ? ''', (propValue,carId))
        self.con.commit()
        self.cur.execute('''SELECT * From Cars WHERE id = ? ''', carId)
        rows = self.cur.fetchall()
        return rows