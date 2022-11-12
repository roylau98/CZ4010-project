import sqlite3
import utilities

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
        setupVault = "CREATE TABLE IF NOT EXISTS vault " \
                     "(title TEXT," \
                     "filename TEXT, " \
                     "hash TEXT, " \
                     "path TEXT," \
                     "iv TEXT," \
                     "updated TEXT," \
                     "uuid TEXT PRIMARY KEY);"
        setupNotes = "CREATE TABLE IF NOT EXISTS notes " \
                     "(title TEXT," \
                     "filename TEXT, " \
                     "hash TEXT, " \
                     "path TEXT," \
                     "iv TEXT," \
                     "updated TEXT," \
                     "uuid TEXT PRIMARY KEY);"
        self.cursor.execute(setupLogin)
        self.cursor.execute(setupVault)
        self.cursor.execute(setupNotes)
        self.connection.commit()

    def fetchAllLogin(self, vaultKey):
        command = "SELECT * FROM login;"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        dict = {}
        for i in data:
            dict[i[5]] = {"account": i[0],
                          "username": i[1],
                          "password": utilities.decrypt(vaultKey, bytes.fromhex(i[2]), bytes.fromhex(i[4])),
                          "updated": i[3],
                          "iv": bytes.fromhex(i[4]),
                          "key": i[5]}
        return dict

    def fetchAllNotes(self):
        command = "SELECT * FROM notes;"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        dict = {}
        for i in data:
            dict[i[6]] = {"title": i[0],
                          "filename": i[1],
                          "hash": i[2],
                          "path": i[3],
                          "iv": bytes.fromhex(i[4]),
                          "updated": i[5],
                          "key": i[6]}
        return dict

    def fetchAllVault(self):
        command = "SELECT * FROM vault;"
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        dict = {}
        for i in data:
            dict[i[6]] = {"title": i[0],
                          "filename": i[1],
                          "hash": i[2],
                          "path": i[3],
                          "iv": bytes.fromhex(i[4]),
                          "updated": i[5],
                          "key": i[6]}
        return dict

    def deleteRecord(self, type, key):
        command = f"DELETE FROM {type} WHERE uuid = (?);"
        data = (key,)
        self.cursor.execute(command, data)
        self.connection.commit()

    def insertRecord(self, type, json):
        if type == "login":
            command = f"INSERT INTO {type} VALUES(?, ?, ?, ?, ?, ?);"
            data = (json["account"], json["username"], json["password"], json["updated"], json["iv"], json["key"],)
        else:
            command = f"INSERT INTO {type} VALUES(?, ?, ?, ?, ?, ?, ?);"
            data = (json["title"], json["filename"], json["hash"], json["path"], json["iv"], json["updated"], json["key"],)
        self.cursor.execute(command, data)
        self.connection.commit()

    def updateRecord(self, type, json):
        if type == "login":
            command = f"UPDATE login " \
                      f"SET account = (?), username = (?), password = (?), updated = (?), iv = (?)" \
                      f"WHERE uuid = (?);"
            data = (json["account"], json["username"], json["password"], json["updated"], json["iv"], json["key"],)
        else:
            command = f"UPDATE {type} " \
                      f"SET title = (?), filename = (?), hash = (?), path = (?), iv = (?), updated = (?)" \
                      f"WHERE uuid = (?);"
            data = (json["title"], json["filename"], json["hash"], json["path"], json["iv"], json["updated"], json["key"],)
        self.cursor.execute(command, data)
        self.connection.commit()