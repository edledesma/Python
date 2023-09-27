class Car:
    def __init__(self, model, brand, year, color,idCar):
        self.model = model
        self.brand = brand
        self.year = year
        self.color = color
        self.idCar = idCar

    def modifyProp(self, prop_name, prop_value):
        if prop_name == "model":
            self.model = prop_value
        elif prop_name == "brand":
            self.brand = prop_value
        elif prop_name == "year":
            self.year = prop_value
        elif prop_name == "color":
            self.color = prop_value
        else:
            print("Invalid property name - Valid properties are model, brand, year, color.")

