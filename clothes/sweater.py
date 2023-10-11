from .clothes import Clothes

class Sweater(Clothes):
    def __init__(self, name, description, serial_number, fabric, price, size, has_zipper, weather1, weather2, department):
        super().__init__(name, description, serial_number, fabric, price, weather1, weather2, department)
        self.has_zipper = has_zipper
        self.size = size