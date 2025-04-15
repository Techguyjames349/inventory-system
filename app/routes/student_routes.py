from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models.student import Student
from app.utils.helpers import generate_student_barcode
import csv
from io import StringIO

student_bp = Blueprint('student', __name__, url_prefix='/students')

@student_bp.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        grade_level = int(request.form.get('grade_level'))
        
        existing_student = Student.query.filter_by(student_id=student_id).first()
        if existing_student:
            flash('Student ID already exists.', 'error')
            return redirect(url_for('student.add_student'))
        
        student = Student(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            grade_level=grade_level
        )
        db.session.add(student)
        try:
            db.session.commit()
            flash('Student added successfully!', 'success')
            return redirect(url_for('student.list_students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding student: {str(e)}', 'error')
    
    return render_template('add_student.html')

@student_bp.route('/list')
def list_students():
    students = Student.query.all()
    return render_template('student_list.html', student_data=students)

@student_bp.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting student: {str(e)}', 'error')
    return redirect(url_for('student.list_students'))

@student_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.student_id = request.form.get('student_id')
        student.first_name = request.form.get('first_name')
        student.last_name = request.form.get('last_name')
        student.grade_level = int(request.form.get('grade_level'))
        
        try:
            db.session.commit()
            flash('Student updated successfully!', 'success')
            return redirect(url_for('student.list_students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating student: {str(e)}', 'error')
    
    return render_template('edit_student.html', student=student)

@student_bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        flash('No file uploaded.', 'error')
        return redirect(url_for('student.list_students'))
    
    try:
        stream = StringIO(file.stream.read().decode('UTF-8'), newline=None)
        csv_reader = csv.DictReader(stream)
        required_columns = ['student_id', 'first_name', 'last_name', 'grade_level']
        
        if not all(col in csv_reader.fieldnames for col in required_columns):
            flash('CSV missing required columns.', 'error')
            return redirect(url_for('student.list_students'))
        
        for row in csv_reader:
            existing_student = Student.query.filter_by(student_id=row['student_id']).first()
            if existing_student:
                continue
            
            student = Student(
                student_id=row['student_id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                grade_level=int(row['grade_level'])
            )
            db.session.add(student)
        
        db.session.commit()
        flash('Students uploaded successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error uploading students: {str(e)}', 'error')
    
    return redirect(url_for('student.list_students'))