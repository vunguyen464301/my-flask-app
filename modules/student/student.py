from flask import Blueprint, request

studentController = Blueprint("student", __name__)


@studentController.route("/student/", methods=["POST"])
def createStudent():
    json_data = request.get_json()
    print(json_data)
    return "ok"


@studentController.route("/student/", methods=["GET"])
def getStudents():
    return "ok"


@studentController.route("/student/<int:studentId>", methods=["GET"])
def getStudentById(studentId):
    print(studentId)
    return "ok"


@studentController.route("/student/<int:studentId>", methods=["PUT"])
def updateStudentById(studentId):
    json_data = request.get_json()
    print(json_data, studentId)
    return "ok"


@studentController.route("/student/<int:studentId>", methods=["DELETE"])
def deleteStudentById(studentId):
    print(studentId)
    return "ok"
