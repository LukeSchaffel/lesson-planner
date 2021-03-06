#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    lessons = db.relationship('Lesson', backref='author', lazy=True)


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class Lesson(db.Model):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    student = db.Column(db.String, nullable=True)
    lessonDate = db.Column(db.Date, nullable=True)
    title = db.Column(db.String, nullable=False)
    subject = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, title, subject, content, user_id, lessonDate, student):
        self.title = title
        self.subject = subject
        self.content = content

        self.user_id = user_id
        self.lessonDate = lessonDate
        self.student = student
       
    
    def __repr__(self):
        return f"Lesson ID: {self.id} -- Date: {self.date} --- Title: {self.Title}"



# ----------------This was never Used---------
# class Student(db.Model):
#     __tablename__ = 'students'
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     name = db.Column(db.String, nullable=False)
#     lessons = db.relationship('Lesson', backref='owner', lazy=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    

#     def __init__(self, name, user_id):
#         self.name = name
#         self.user_id = user_id


    
#     def __repr__(self):
#         return f"Lesson ID: {self.id} -- Date: {self.date} --- Title: {self.Name}"        