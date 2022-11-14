import sqlite3

class DataBase:
    def __init__(self, database):
        self.database = database
        self.connect()
        self.setup()

    def connect(self):
        self.connection = sqlite3.connect(self.database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    def setup(self):
        setupUsers = "CREATE TABLE IF NOT EXISTS users " \
                     "(auth TEXT PRIMARY KEY," \
                     "lastLogin TEXT, " \
                     "filehash TEXT);"
        self.cursor.execute(setupUsers)
        self.connection.commit()

    def retrieveUser(self, user):
        command = "SELECT * FROM users WHERE auth = (?);"
        data = (user,)
        self.cursor.execute(command, data)
        results = self.cursor.fetchone()
        if results != None:
            results = {"auth": results[0],
                       "lastLogin": results[1],
                       "hash": results[2]}
        self.connection.commit()
        return results

    def insertUser(self, json):
        command = "INSERT INTO users VALUES (?, ?, ?)"
        data = (json["auth"], json["lastLogin"], json["filehash"],)
        self.cursor.execute(command, data)
        self.connection.commit()