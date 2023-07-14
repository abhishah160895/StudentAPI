from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class student(db.Model):
    StudentId = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(250), nullable=False)
    LastName = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.Date, nullable=True)
    Amount_Due = db.Column(db.Integer, nullable=True)


