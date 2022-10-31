import pyrebase

config = {
  "<change me>"
}

class Firebase:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

    def registerUser(self, auth):
        self.db.child(auth).set({"auth": auth})


    def getLoginDetails(self, auth):
        logins = self.db.child("users/"+auth).get()
        for login in logins:
            print(login)
        print(logins)

if __name__=='__main__':
    firebase = Firebase()