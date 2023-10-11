from .seasons import Season

class Cool_Weather(Season):
    def __init__(self, name):
        super().__init__(name)
        self.avg_temp = 70
        