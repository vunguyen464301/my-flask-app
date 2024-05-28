from flask import Flask, request
from flask_restx import Api, fields, Resource, Namespace

from modules.database import dbConnection
from modules.student import studentNs

app = Flask(__name__)

helloNs = Namespace("hello", description="Hello World operation")
helloModel = helloNs.model(
    "HelloModel",
    {"message": fields.String(required=True, description="Hello message")},
)


@helloNs.route("/")
class HelloWorld(Resource):
    @helloNs.response(200, "Success", helloModel)
    def get(self):
        """
        Get a hello world message
        """
        return {"message": "Hello, World!"}


@helloNs.route("/connection")
class Connection(Resource):
    @helloNs.response(200, "Success", helloModel)
    def get(self):
        # Create a cursor
        cursor = dbConnection.cursor()

        # Execute the query
        cursor.execute("SELECT @@VERSION")

        # Fetch the result
        row = cursor.fetchone()
        return f"Connected to SQL Server. Server version: { row[0]}"


# app.register_blueprint(studentModuleView)
api = Api(app, version="1.0", title="Student API", description="A simple Student API")
api.add_namespace(helloNs)
api.add_namespace(studentNs)

if __name__ == "__main__":
    app.run(debug=True)
