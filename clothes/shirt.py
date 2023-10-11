from .clothes import Clothes

class Shirt(Clothes):
    def __init__(self, name, description, serial_number, fabric, price, size, has_sleeves, weather1, weather2, department):
        super().__init__(name, description, serial_number, fabric, price, weather1, weather2, department)
        self.has_sleeves = has_sleeves
        self.size = size
        