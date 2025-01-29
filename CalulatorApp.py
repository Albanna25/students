from flask import Flask, request
from markupsafe import escape
import json


app = Flask(__name__)

students = ["Ameen", "Khaled", "Ali"]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/students/", methods = ['GET'])
def users():

    response_json = {"response": "All good!", "data": students}
    return json.dumps(response_json)
    #fullstudentlist = ""

    #for student_name in students:
    #    fullstudentlist = fullstudentlist + "\n" + student_name 

    #return fullstudentlist
@app.route("/add-students", methods = ['POST'])
def addstudent():
    request_data = request.get_json()
    students.append(request_data["name"])
    return students

@app.route("/add")
def newuser():
    newuser = input("Enter your name")
    return f"<p>Hello, {newuser}</p>"

#Another route (new student name)

@app.route('/students/<username>')
def show_user_profile(username):
    students.append(username)
    return f'User {escape(username)}'




