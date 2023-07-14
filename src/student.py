import json
from flask import Blueprint, request, jsonify
from flasgger import swag_from


from constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT
from database import student, db
from datamodel.student import studentBO
from json_utility import json_default

studentBlueprint = Blueprint("auth", __name__, url_prefix="/api/v1/student")


@studentBlueprint.post('/addstudent')
@swag_from('./docs/student/addstudent.yaml')
def addNewStudent():
    firstName = request.json['FirstName']
    lastName = request.json['LastName']
    DOB = request.json['DOB']
    Amount_due = request.json['Amount_Due']

    std = student(StudentId = None, FirstName= firstName, LastName = lastName, DOB= DOB, Amount_Due = Amount_due)
    db.session.add(std)
    db.session.commit()
    return jsonify({
        'message': "Stduent created successfully",
        'student': {
            'First Name': std.FirstName
        }
    }), HTTP_201_CREATED

@studentBlueprint.get('/getAllStudents')
@swag_from('./docs/student/getallstudents.yaml')
def getAllstudents():
    studentlst = db.session.query(student).filter_by().all()
    lst = []
    for x in studentlst:
        obj = studentBO(x.StudentId, x.FirstName, x.LastName, x.DOB, x.Amount_Due)
        obj.setObjFromOrMObj(x)
        lst.append(obj)

    jsonstr = json.dumps(lst, default=json_default, indent=4)
    return jsonstr, HTTP_200_OK

@studentBlueprint.delete('/deleteStudent')
@swag_from('./docs/student/deletestudent.yaml')
def deletestudent():
    student_fName = request.json['FirstName']
    student_LName = request.json['LastName']
    db.session.query(student).filter_by(FirstName = student_fName, LastName = student_LName).delete()
    db.session.commit()
    return jsonify({
        'message': "Student deleted successfully",
        'student': {
            'First Name': student_fName,
            'Last Name' : student_LName
        }
    }), HTTP_200_OK

@studentBlueprint.patch('/updateStudent')
@swag_from('./docs/student/updatestudent.yaml')
def updateStudentInfo():
    student_Id = request.json['StudentId']
    firstName = request.json['FirstName']
    lastName = request.json['LastName']
    DOB = request.json['DOB']
    Amount_due = request.json['Amount_Due']

    std = db.session.query(student).filter_by(StudentId = student_Id).first()
    if(firstName is not None):
        std.FirstName = firstName
    if (lastName is not None):
        std.LastName = lastName
    if (DOB is not None):
        std.DOB = DOB

    if(Amount_due is not None):
        std.Amount_due = Amount_due

    db.session.commit()

    return jsonify({
        'message': "Student Updated successfully",
        'student': {
            'First Name': firstName,
            'Last Name': lastName,
            'DOB' : DOB,
            'Amount_due' : Amount_due
        }
    }), HTTP_200_OK