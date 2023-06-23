import sqlite3


class SQLHandling:
    def __init__(self, database):
        self.my_conn = sqlite3.connect(database)
        self.cursor = self.my_conn.cursor()

    def execute(self, query, *args):
        self.cursor.execute(query, *args)
        self.my_conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def executemany(self, query, data):
        self.cursor.executemany(query, data)
        self.my_conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.my_conn.close()
