from datetime import date

class Clothes:
    def __init__(self, name, description, serial_number, fabric, price, weather1, weather2, department):
        self.name = name
        self.description = description
        self.__serial_number = serial_number
        self.fabric = fabric
        self.price = price
        self.date_added = date.today()
        self.department = []
        self.weather = [weather1, weather2]
        self.department = department
        weather1.articles.append(self)
        weather2.articles.append(self)
        department.articles.append(self)

    @property
    def serial_number(self):
        return self.__serial_number
    @serial_number.setter
    def serial_number(self, num):
        pass
    def __str__(self):
        return f"{self.name} is a part of the {self.weather[0].name} and {self.weather[1].name} collection. {self.name} can be located in the {self.department.name} department"
    