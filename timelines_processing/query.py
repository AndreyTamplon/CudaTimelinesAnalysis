class Query:
    def __init__(self, path):
        self.query = None
        self.path = path

    def open(self):
        self.query = open(self.path, "r").read()

    def get_query(self):
        return self.query
