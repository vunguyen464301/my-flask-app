from flask import Flask, request
from flask_restx import Api, fields, Resource, Namespace
from modules.student import studentModuleView

app = Flask(__name__)

helloNs = Namespace("hello", description="Hello World operation")
helloModel = helloNs.model(
    "HelloModel",
    {"message": fields.String(required=True, description="Hello message")},
)


@helloNs.route("/")
@helloNs.response(200, "Success", helloModel)
class HelloWorld(Resource):
    @helloNs.response(200, "Success", helloModel)
    def get(self):
        """
        Get a hello world message
        """
        return {"message": "Hello, World!"}


@app.route("/connection")
def index():
    # cursor = dbConnection.cursor()
    # cursor.execute("SELECT @@version")
    # row = cursor.fetchone()
    # return f"Connected to SQL Server. Server version: {row[0]}"
    return "not ok"


app.register_blueprint(studentModuleView)
api = Api(app)
api.add_namespace(helloNs)


if __name__ == "__main__":
    app.run(debug=True)
