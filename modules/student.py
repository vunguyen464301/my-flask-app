from flask import Blueprint, request
from flask_restx import Api, fields, Resource, Namespace

studentNs = Namespace("student", description="Hello World operation")
studentModel = studentNs.model(
    "StudenModel",
    {
        "name": fields.String(required=True, description="The student name"),
        "age": fields.Integer(required=True, description="The student age"),
        "gender": fields.String(required=True, description="The student gender"),
    },
)
# Define the model for the response message
messageModel = studentNs.model(
    "MessageModel", {"message": fields.String(required=True, description="ABC")}
)


@studentNs.route("/")
class StudentModule(Resource):
    @studentNs.response(200, "Success", studentModel)
    def get(self):
        return "ok"

    @studentNs.expect(studentModel)
    @studentNs.response(201, "Created", messageModel)
    def post(self):
        json_data = request.get_json()
        print(json_data)
        return "ok"


@studentNs.route("/<int:id>")
class StudentModule(Resource):
    @studentNs.response(200, "Success", studentModel)
    def get(self, id):
        return "ok"

    @studentNs.expect(studentModel)
    @studentNs.response(200, "Success", studentModel)
    def put(self, id):
        return "ok"

    @studentNs.response(200, "Success", studentModel)
    def delete(self, id):
        return "ok"
