from flask import Blueprint, render_template, request, redirect, url_for, make_response
from app import db
from app.models.item import Item, Chromebook, PowerAdapter, Bag
from app.models.student import Student
from app.models.assignment import Assignment
from app.utils.helpers import generate_student_barcode
from datetime import datetime, timedelta
import csv
from io import StringIO

# Add basic logging for debugging
import logging
logging.basicConfig(level=logging.DEBUG)

item_bp = Blueprint('item', __name__)

@item_bp.route('/', methods=['GET'])
def home():
    filter_type = request.args.get('filter_type', 'all')
    if filter_type == 'all':
        items = Item.query.all()
    else:
        items = Item.query.filter_by(type=filter_type).all()
    item_data = []
    for item in items:
        current_student = Student.query.get(item.current_student_id) if item.current_student_id else None
        student_name = f"{current_student.first_name} {current_student.last_name}" if current_student else "Unassigned"
        item_data.append({
            'item': item,
            'current_student_name': student_name
        })
    return render_template('index.html', item_data=item_data, filter_type=filter_type)

@item_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_type = request.form['item_type']
        
        # Define barcode prefixes
        barcode_prefix = {
            'chromebook': 'USD349-CB-',
            'power_adapter': 'USD349-PWR-',
            'bag': 'USD349-BAG-'
        }.get(item_type, 'USD349-')
        
        # Find the highest numeric part for this item type
        items_of_type = Item.query.filter_by(type=item_type).all()
        max_number = 0
        for item in items_of_type:
            if item.barcode.startswith(barcode_prefix):
                try:
                    num = int(item.barcode.split('-')[-1])
                    max_number = max(max_number, num)
                except (ValueError, IndexError):
                    continue
        new_number = max_number + 1
        barcode = f"{barcode_prefix}{new_number:05d}"
        
        # Get common fields for all items
        received_date = datetime.strptime(request.form['received_date'], '%Y-%m-%d').date() if request.form['received_date'] else None
        
        # Create the appropriate item type
        if item_type == 'chromebook':
            serial_number = request.form['serial_number']
            model = request.form['model']
            overall_condition = request.form['overall_condition']
            bezel_condition = request.form['bezel_condition']
            hinge_cap = request.form['hinge_cap']
            provisioned_date = datetime.strptime(request.form['provisioned_date'], '%Y-%m-%d').date() if request.form['provisioned_date'] else None
            
            refresh_date_option = request.form.get('refresh_option', 'auto')
            if refresh_date_option == 'auto':
                refresh_date = received_date + timedelta(days=5*365) if received_date else None
            else:
                refresh_date = datetime.strptime(request.form.get('refresh_date', ''), '%Y-%m-%d').date() if request.form.get('refresh_date') else None
            
            disposition = request.form.get('disposition', None)
            
            item = Chromebook(
                barcode=barcode,
                serial_number=serial_number,
                model=model,
                condition=overall_condition,  # Use overall condition as the general condition
                overall_condition=overall_condition,
                bezel_condition=bezel_condition,
                hinge_cap=hinge_cap,
                received_date=received_date,
                provisioned_date=provisioned_date,
                refresh_date=refresh_date,
                disposition=disposition
            )
        elif item_type == 'power_adapter':
            serial_number = request.form['serial_number']
            model = request.form['model']
            condition = request.form.get('condition', 'Good')
            
            item = PowerAdapter(
                barcode=barcode,
                serial_number=serial_number,
                model=model,
                received_date=received_date,
                condition=condition
            )
        elif item_type == 'bag':
            condition = request.form.get('condition', 'Good')
            
            item = Bag(
                barcode=barcode,
                serial_number=None,
                model=None,
                received_date=received_date,
                condition=condition
            )
        else:
            serial_number = request.form.get('serial_number', '')
            model = request.form.get('model', '')
            condition = request.form.get('condition', 'Good')
            
            item = Item(
                barcode=barcode,
                serial_number=serial_number,
                model=model,
                type=item_type,
                received_date=received_date,
                condition=condition
            )
        
        print(f"Creating new item with barcode: {barcode}")
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))
    
    # For GET request, prepare the form
    today = datetime.today().strftime('%Y-%m-%d')
    
    # Calculate the next barcode for the default type (Chromebook) to show in the form
    chromebook_prefix = 'USD349-CB-'
    chromebooks = Item.query.filter_by(type='chromebook').all()
    max_chromebook_number = 0
    for cb in chromebooks:
        if cb.barcode.startswith(chromebook_prefix):
            try:
                num = int(cb.barcode.split('-')[-1])
                max_chromebook_number = max(max_chromebook_number, num)
            except (ValueError, IndexError):
                continue
    next_number = max_chromebook_number + 1
    next_barcode = f"USD349-CB-{next_number:05d}"
    
    return render_template('add_item.html', today=today, next_barcode=next_barcode)

@item_bp.route('/lookup', methods=['GET'])
def lookup():
    lookup_type = request.args.get('lookup_type')
    identifier = request.args.get('identifier')
    if lookup_type == 'barcode':
        item = Item.query.filter_by(barcode=identifier).first()
    else:
        item = Item.query.filter_by(serial_number=identifier).first()
    if not item:
        return render_template('item_detail.html', item=None)
    current_student = Student.query.get(item.current_student_id) if item.current_student_id else None
    assignments = Assignment.query.filter_by(chromebook_id=item.id).order_by(Assignment.checkout_date.desc()).all()
    
    # Debug logging to inspect assignments
    logging.debug(f"Item: {item.barcode}, Current Student ID: {item.current_student_id}")
    for assignment in assignments:
        student_info = f"{assignment.student.first_name} {assignment.student.last_name}" if hasattr(assignment, 'student') and assignment.student else "No Student"
        logging.debug(f"Assignment ID: {assignment.id}, Student ID: {assignment.student_id}, Student: {student_info}")
        if assignment.student_id and not hasattr(assignment, 'student'):
            logging.error(f"Assignment {assignment.id} has student_id {assignment.student_id} but no student relationship")
        elif assignment.student_id and not assignment.student:
            logging.error(f"Student ID {assignment.student_id} has no corresponding Student object")
    
    return render_template('item_detail.html', item=item, current_student=current_student, assignments=assignments)

@item_bp.route('/checkout/<barcode>', methods=['GET', 'POST'])
def checkout(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        return redirect(url_for('item.home'))
    if item.current_student_id:
        return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))
    
    # Load all students for initial display and filtering
    students = Student.query.order_by(Student.last_name, Student.first_name).all()
    
    if request.method == 'POST':
        search_query = request.form.get('search_query', '').strip().lower()
        grade_level = request.form.get('grade_level', '').strip()
        
        # Filter students based on search query and grade level
        filtered_students = []
        for student in students:
            full_name = f"{student.first_name} {student.last_name}".lower()
            matches_search = not search_query or search_query in full_name or search_query in student.student_id.lower()
            # Normalize grade_level by converting to integer (handles "06" vs "6")
            student_grade = int(student.grade_level)  # Convert "06" to 6
            filter_grade = int(grade_level) if grade_level else None
            matches_grade = not grade_level or student_grade == filter_grade
            if matches_search and matches_grade:
                filtered_students.append(student)
        
        logging.debug(f"Search Query: '{search_query}', Grade Filter: '{grade_level}', Filtered Students: {len(filtered_students)}")
        return render_template('checkout.html', item=item, students=filtered_students, search_query=search_query, grade_level=grade_level)
    
    # On GET, pass all students for JavaScript to handle initial filtering
    return render_template('checkout.html', item=item, students=students, search_query='', grade_level='')

@item_bp.route('/checkout/<barcode>/confirm', methods=['POST'])
def checkout_confirm(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        return redirect(url_for('item.home'))
    student_id = request.form.get('student_id')
    student = Student.query.get(student_id)
    if not student:
        return redirect(url_for('item.checkout', barcode=barcode))
    item.current_student_id = student.id
    item.student_barcode = generate_student_barcode(student)
    assignment = Assignment(
        chromebook_id=item.id,
        student_id=student.id,
        student_barcode=item.student_barcode,
        checkout_date=datetime.now(),
        grade_at_checkout=student.grade_level
    )
    db.session.add(assignment)
    db.session.commit()
    return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

@item_bp.route('/checkin/<barcode>', methods=['POST'])
def checkin(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        return redirect(url_for('item.home'))
    assignment = Assignment.query.filter_by(chromebook_id=item.id, checkin_date=None).first()
    if assignment:
        assignment.checkin_date = datetime.now()
        item.current_student_id = None
        item.student_barcode = None
        db.session.commit()
    return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

@item_bp.route('/upload_inventory', methods=['GET', 'POST'])
def upload_inventory():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            return redirect(request.url)
        
        # Read and process the CSV file
        content = file.stream.read().decode("UTF-8")
        stream = StringIO(content)
        csv_reader = csv.DictReader(stream)
        
        print(f"CSV Headers: {csv_reader.fieldnames}")
        
        # Process each row in the CSV
        for row in csv_reader:
            # Skip if item already exists
            existing_item = Item.query.filter(
                (Item.barcode == row['barcode']) | 
                (Item.serial_number == row['serial_number'] if row.get('serial_number') else False)
            ).first()
            
            if existing_item:
                print(f"Skipping existing item: {row['barcode']}")
                continue
            
            # Parse the dates
            received_date = datetime.strptime(row['received_date'], '%Y-%m-%d').date() if row.get('received_date') else None
            refresh_date = datetime.strptime(row['refresh_date'], '%Y-%m-%d').date() if row.get('refresh_date') else None
            
            # Create the appropriate item based on type
            item_type = row.get('type', '').lower()
            
            if item_type == 'chromebook':
                # Log condition values from CSV
                print(f"Creating Chromebook with conditions - Overall: '{row.get('overall_condition')}', Bezel: '{row.get('bezel_condition')}', Hinge: '{row.get('hinge_cap')}'")
                
                # Create a Chromebook
                item = Chromebook(
                    barcode=row['barcode'],
                    serial_number=row['serial_number'],
                    model=row['model'],
                    condition=row.get('overall_condition', 'Unknown'),  # Set general condition
                    overall_condition=row.get('overall_condition'),
                    bezel_condition=row.get('bezel_condition'),
                    hinge_cap=row.get('hinge_cap'),
                    received_date=received_date,
                    refresh_date=refresh_date,
                    quantity=int(row.get('quantity', 1))
                )
            elif item_type == 'power_adapter':
                item = PowerAdapter(
                    barcode=row['barcode'],
                    serial_number=row.get('serial_number'),
                    model=row.get('model'),
                    received_date=received_date,
                    condition=row.get('condition', 'Good'),
                    quantity=int(row.get('quantity', 1))
                )
            elif item_type == 'bag':
                item = Bag(
                    barcode=row['barcode'],
                    serial_number=None,  # Bags don't have serial numbers
                    model=None,  # Bags don't have model numbers
                    received_date=received_date,
                    condition=row.get('condition', 'Good'),
                    quantity=int(row.get('quantity', 1))
                )
            else:
                # Handle non-specific item types
                item = Item(
                    barcode=row['barcode'],
                    serial_number=row.get('serial_number'),
                    model=row.get('model'),
                    type=item_type,
                    condition=row.get('condition', 'Good'),
                    received_date=received_date,
                    quantity=int(row.get('quantity', 1))
                )
            
            # Add and commit the item
            db.session.add(item)
            try:
                db.session.commit()
                print(f"Added item: {row['barcode']}")
                
                # Handle student assignment if needed for Chromebooks
                if item_type == 'chromebook':
                    student_name = row.get('student_name') or row.get('Assigned To')  # Check common name columns
                    if student_name:
                        # Split name into first and last, assuming "First Last" format
                        name_parts = student_name.strip().split()
                        if len(name_parts) >= 2:
                            first_name = name_parts[0]
                            last_name = " ".join(name_parts[1:])  # Handle multi-part last names
                            student = Student.query.filter_by(first_name=first_name, last_name=last_name).first()
                        else:
                            print(f"Invalid student name format for {row['barcode']}: {student_name}")
                            continue
                        
                        if student:
                            chromebook = Chromebook.query.filter_by(barcode=row['barcode']).first()
                            chromebook.current_student_id = student.id
                            chromebook.student_barcode = generate_student_barcode(student)
                            
                            assignment = Assignment(
                                chromebook_id=chromebook.id,
                                student_id=student.id,
                                student_barcode=chromebook.student_barcode,
                                checkout_date=datetime.now(),
                                grade_at_checkout=student.grade_level
                            )
                            
                            db.session.add(assignment)
                            db.session.commit()
                            print(f"Assigned student {student_name} (ID: {student.id}) to {row['barcode']}")
                        else:
                            print(f"Student not found for {row['barcode']}: {student_name}")
                    elif row.get('student_id'):  # Fallback to student_id if present
                        try:
                            student_id_value = str(int(float(row['student_id']))) if row['student_id'] else None
                            if student_id_value:
                                student = Student.query.filter_by(student_id=student_id_value).first()
                                if student:
                                    chromebook = Chromebook.query.filter_by(barcode=row['barcode']).first()
                                    chromebook.current_student_id = student.id
                                    chromebook.student_barcode = generate_student_barcode(student)
                                    
                                    assignment = Assignment(
                                        chromebook_id=chromebook.id,
                                        student_id=student.id,
                                        student_barcode=chromebook.student_barcode,
                                        checkout_date=datetime.now(),
                                        grade_at_checkout=student.grade_level
                                    )
                                    
                                    db.session.add(assignment)
                                    db.session.commit()
                                    print(f"Assigned student ID {student_id_value} to {row['barcode']}")
                                else:
                                    print(f"Student ID {student_id_value} not found for {row['barcode']}")
                        except (ValueError, TypeError) as e:
                            print(f"Error processing student ID for {row['barcode']}: {e}")
            except Exception as e:
                print(f"Error saving item {row['barcode']}: {e}")
                db.session.rollback()
                
        return redirect(url_for('item.home'))
    
    return render_template('upload_inventory.html')

@item_bp.route('/export_inventory', methods=['GET'])
def export_inventory():
    items = Item.query.all()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['barcode', 'serial_number', 'model', 'type', 'received_date', 'condition', 'overall_condition', 'bezel_condition', 'hinge_cap', 'refresh_date', 'current_student'])
    for item in items:
        current_student = Student.query.get(item.current_student_id) if item.current_student_id else None
        student_name = f"{current_student.first_name} {current_student.last_name}" if current_student else "Unassigned"
        
        if item.type == 'chromebook':
            writer.writerow([
                item.barcode,
                item.serial_number,
                item.model,
                item.type,
                item.received_date,
                item.condition,
                item.overall_condition,
                item.bezel_condition,
                item.hinge_cap,
                item.refresh_date,
                student_name
            ])
        else:
            writer.writerow([
                item.barcode,
                item.serial_number or '',
                item.model or '',
                item.type,
                item.received_date,
                item.condition,
                'N/A', 'N/A', 'N/A', 'N/A',
                student_name
            ])
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=inventory.csv'
    response.headers['Content-type'] = 'text/csv'
    return response

@item_bp.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('item.home'))