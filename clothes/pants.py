from .clothes import Clothes

class Pants(Clothes):
    def __init__(self, name, description, serial_number, fabric, price, pant_width, pant_length, weather1, weather2, department):
        super().__init__(name, description, serial_number, fabric, price, weather1, weather2, department)
        self.pant_width = pant_width
        self.pant_length = pant_length
        