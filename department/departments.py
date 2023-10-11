from datetime import date

class Departments: 
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.date_added = date.today()
        self.articles = []
    def print(self):
        print(f"{self.name} department contains:")
        for article in self.articles:
            print(f"* {article.name}")
