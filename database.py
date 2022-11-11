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
        setupLogin = "CREATE TABLE IF NOT EXISTS login " \
                     "(account TEXT," \
                     "username TEXT, " \
                     "password TEXT, " \
                     "updated TEXT," \
                     "iv TEXT," \
                     "uuid TEXT PRIMARY KEY);"
        self.cursor.execute(setupLogin)
        self.connection.commit()

    def fetchAllLogin(self):
        command = "SELECT * " \
                  "FROM login;"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        dict = {}
        for i in data:
            dict[i[5]] = {"account": i[0],
                          "username": i[1],
                          "password": i[2],
                          "updated": i[3],
                          "iv": i[4],
                          "key": i[5]}
        return dict

    def deleteRecord(self, type, key):
        command = f"DELETE FROM {type} WHERE uuid = (?);"
        data = (key,)
        self.cursor.execute(command, data)
        self.connection.commit()

    def insertRecord(self, type, json):
        command = f"INSERT INTO {type} VALUES(?, ?, ?, ?, ?, ?);"
        if type == "login":
            data = (json["account"], json["username"], json["password"], json["updated"], json["iv"], json["key"],)
        self.cursor.execute(command, data)
        self.connection.commit()

    def updateRecord(self, type, json):
        if type == "login":
            command = f"UPDATE login " \
                      f"SET account = (?), username = (?), password = (?), updated = (?), iv = (?)" \
                      f"WHERE uuid = (?);"
            data = (json["account"], json["username"], json["password"], json["updated"], json["iv"], json["key"],)
        self.cursor.execute(command, data)
        self.connection.commit()