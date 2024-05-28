from flask import Flask, request

# from modules.course import course
from modules.student.student import studentController

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


# course()
app.register_blueprint(studentController)


if __name__ == "__main__":
    app.run(debug=True)
