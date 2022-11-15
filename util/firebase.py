import pyrebase
from datetime import datetime

config = {
    "apiKey": "AIzaSyC5V-T1vTjNe2LxetrCbEefB3m5tTVsXDo",
    "authDomain": "cz4010-3578d.firebaseapp.com",
    "databaseURL": "https://cz4010-3578d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cz4010-3578d",
    "storageBucket": "cz4010-3578d.appspot.com",
}

class Firebase:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    def registerUser(self, auth):
        self.db.child(auth).set({"auth": auth,
                                 "lastLogin": datetime.now().strftime('%d %b %Y, %I:%M %p')})

    def authenticate(self, auth):
        if self.db.child(auth).get().val():
            lastLogin = self.db.child(auth+"/lastLogin").get().val()
            self.db.child(auth).update({"lastLogin": datetime.now().strftime('%d %b %Y, %I:%M %p')})
            return lastLogin
        else:
            return None

    def getLoginDetails(self, auth):
        logins = self.db.child("users/"+auth).get()
        for login in logins:
            print(login)
        print(logins)

if __name__=='__main__':
    firebase = Firebase()