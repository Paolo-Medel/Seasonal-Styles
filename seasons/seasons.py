class Season:
    def __init__(self, name):
        self.name = name
        self.articles = []
    def print(self):
        print(f'The {self.name} collection includes:')
        for article in self.articles:
            print(f'* {article.name}')
        