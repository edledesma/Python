'''
Car Database Access Object
'''
import sqlite3

class CarDao:
    '''
    TEST
    '''
    #Connects to the database, creates a cursor and calls the function that creates it if it doesn't exist
    def __init__(self):
        self.con = sqlite3.connect('src/Data/cars.db')
        self.cur = self.con.cursor()
        self.create_car_table()
    
    def create_car_table(self):
        '''
        TEST
        '''
        self.cur.execute("""CREATE TABLE IF NOT EXISTS cars(id INTEGER PRIMARY KEY AUTOINCREMENT, model TEXT, brand TEXT, year INTEGER, color TEXT, isActive TEXT DEFAULT 'True')""")
        self.con.commit()

    def insert_car(self, item):
        '''
        TEST
        '''
        self.cur.execute("""INSERT INTO cars(model, brand, year, color) VALUES(?,?,?,?)""", item)
        self.con.commit()

    def read_car(self,car_id):
        '''
        TEST
        '''
        self.cur.execute("""SELECT *FROM cars WHERE id = ?""" ,(car_id,))
        rows = self.cur.fetchall()
        return rows

    def read_cars(self):
        '''
        TEST
        '''
        self.cur.execute("""SELECT *FROM cars WHERE isActive = 'True' """)
        rows = self.cur.fetchall()
        return rows

    def delete_car(self,car_id):
        '''
        TEST
        '''
        self.cur.execute("""UPDATE cars SET isActive = 'False' WHERE id = ? """,(car_id,))
        self.con.commit()

    def modify_car(self,car_id,prop_modify, prop_value):
        '''
        TEST
        '''
        self.cur.execute(f""" UPDATE cars SET  {prop_modify} = ? WHERE id = (?) """, (prop_value,car_id))
        self.con.commit()
        self.cur.execute("""SELECT * From Cars WHERE id = ? """, (car_id,))
        rows = self.cur.fetchall()
        return rows
    