class TimelineDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def open(self):
        import sqlite3
        self.conn = sqlite3.connect(self.db_path)
        if self.conn is None:
            raise Exception("Failed to open database")
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
