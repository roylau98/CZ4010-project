from flask import Flask, request, jsonify, make_response
# from flask_cors import CORS
from database import DataBase

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        # CORS(self.app)
        self.db = DataBase("server.db")

        @self.app.route('/<string:user>', methods=["GET"])
        def requestQuery(user):
            results = self.db.retrieveUser(user)
            return jsonify(results)

        @self.app.route("/register", methods=["POST", "GET"])
        def registerUser():
            data = request.json
            self.db.insertUser(data)
            return make_response("", 200)

        @self.app.route("/update", methods=["POST", "PUT"])
        def updateData():
            data = request.json
            self.db.updateValues(data)
            return make_response("", 200)

    def run(self):
        self.app.run()
