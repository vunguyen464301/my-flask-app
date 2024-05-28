from flask import Flask, request
from modules.database.sqlServer import dbConnection

# from modules.course import course
from modules.student.student import studentController

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


# Sample route to test database connection
@app.route("/connection")
def index():
    cursor = dbConnection.cursor()
    cursor.execute("SELECT @@version")
    row = cursor.fetchone()
    return f"Connected to SQL Server. Server version: {row[0]}"


# course()
app.register_blueprint(studentController)


if __name__ == "__main__":
    app.run(debug=True)
