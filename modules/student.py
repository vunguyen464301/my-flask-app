from flask import Blueprint, request


studentModuleView = Blueprint("student", __name__, url_prefix="/student")


class StudentModule:
    @studentModuleView.route("/", methods=["POST"])
    def createStudent(self):
        json_data = request.get_json()
        print(json_data)
        return "ok"

    @studentModuleView.route("/", methods=["GET"])
    def getStudents(self):
        return "ok"

    @studentModuleView.route("/<int:studentId>", methods=["GET"])
    def getStudentById(self, studentId):
        print(studentId)
        return "ok"

    @studentModuleView.route("/<int:studentId>", methods=["PUT"])
    def updateStudentById(self, studentId):
        json_data = request.get_json()
        print(json_data, studentId)
        return "ok"

    @studentModuleView.route("/<int:studentId>", methods=["DELETE"])
    def deleteStudentById(self, studentId):
        print(studentId)
        return "ok"
