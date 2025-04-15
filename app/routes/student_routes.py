from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.student import Student
from app.utils.helpers import generate_student_barcode
import csv
from io import StringIO

student_bp = Blueprint('student', __name__)

@student_bp.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student = Student(
            student_id=request.form['student_id'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            grade_level=request.form['grade_level']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student.list_students'))
    return render_template('add_student.html')

@student_bp.route('/list', methods=['GET', 'POST'])
def list_students():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file:
            stream = StringIO(file.stream.read().decode("UTF-8"))
            csv_reader = csv.DictReader(stream)
            for row in csv_reader:
                try:
                    student = Student.query.filter_by(student_id=row['Student Id']).first()
                    if student:
                        student.first_name = row['Student First Name']
                        student.last_name = row['Student Last Name']
                        student.grade_level = row['Grade Level Code']
                    else:
                        student = Student(
                            student_id=row['Student Id'],
                            first_name=row['Student First Name'],
                            last_name=row['Student Last Name'],
                            grade_level=row['Grade Level Code']
                        )
                        db.session.add(student)
                except KeyError as e:
                    return f"Missing required column: {e}", 400
            db.session.commit()
            return redirect(url_for('student.list_students'))
    students = Student.query.all()
    # Generate barcodes for each student
    student_data = []
    for student in students:
        barcode = generate_student_barcode(student)
        student_data.append({
            'student': student,
            'barcode': barcode
        })
    return render_template('student_list.html', student_data=student_data)

@student_bp.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('student.list_students'))

@student_bp.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.student_id = request.form['student_id']
    student.first_name = request.form['first_name']
    student.last_name = request.form['last_name']
    student.grade_level = request.form['grade_level']
    db.session.commit()
    return redirect(url_for('student.list_students'))