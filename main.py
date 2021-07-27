import os
from flask import Flask, render_template, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, 
	                 RadioField, SelectField, TextField, TextAreaField, IntegerField)
from wtforms.validators import DataRequired 



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask (__name__)

app.config['SECRET_KEY'] = 'anothersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class StudentForm(FlaskForm):
	name = StringField ('Enter full name:', validators = [DataRequired()])
	grade = IntegerField ('Enter final grade:', validators = [DataRequired()])
	submit = SubmitField('Submit')

# class deleteForm(FlaskForm):
# 	deleteId = IntegerField('Enter id number of the name you want to delete:', validators = [DataRequired()])
# 	submit = SubmitField('Submit')

"""
Create Student databse 
"""
class Student(db.Model):
	__tablename__="students"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	grade = db.Column(db.Integer)

	def __init__(self, name, grade):
		self.name = name 
		self.grade = grade

	def __repr__(self):
		return f"(id:{self.id}, name:{self.name}, grade:{self.grade})"

"""

"""
@app.route ('/', methods = ['GET', 'POST'])
def index ():
	form = StudentForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		session['grade'] = form.grade.data
		new_student = Student (form.name.data, form.grade.data)
		db.session.add(new_student)
		db.session.commit()

	return render_template('main.html', form = form, )




"""

"""
@app.route ('/students')
def allStudents():
	allStudents = Student.query.all()
	return render_template('results1.html', allStudents = allStudents)
"""

"""
@app.route ('/PassFail')
def passFail():
	pass_fail = Student.query.filter(Student.grade >= 70)
	pass_failAll = pass_fail.all()
	return render_template('results.html', pass_failAll = pass_failAll)



if __name__ == '__main__':
	app.run(debug = True)