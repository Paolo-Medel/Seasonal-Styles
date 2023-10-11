from .clothes import Clothes

class Undies(Clothes):
    def __init__(self, name, description, serial_number, fabric, price, size, weather1, weather2, department):
        super().__init__(name, description, serial_number, fabric, price, weather1, weather2, department)
        self.size = size