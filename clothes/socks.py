from .clothes import Clothes

class Socks(Clothes):
    def __init__(self, name, description, serial_number, fabric, price, is_long, weather1, weather2, department):
        super().__init__(name, description, serial_number, fabric, price, weather1, weather2, department)
        self.is_long = is_long
        