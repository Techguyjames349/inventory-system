from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from app import db
from app.models.item import Item, Chromebook, PowerAdapter, Bag
from app.models.student import Student
from app.models.assignment import Assignment
from datetime import datetime, timedelta
import csv
from io import StringIO
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

item_bp = Blueprint('item', __name__, url_prefix='/items')

@item_bp.route('/')
def home():
    query = Item.query
    barcode = request.args.get('barcode', '').strip()
    serial = request.args.get('serial', '').strip()
    model = request.args.get('model', '').strip()
    condition = request.args.get('condition', '').strip()
    assigned_to = request.args.get('assigned_to', '').strip()
    type_filter = request.args.get('type', '').strip()

    if barcode:
        query = query.filter(Item.barcode.ilike(f'%{barcode}%'))
    if serial:
        query = query.filter(Item.serial_number.ilike(f'%{serial}%'))
    if model:
        query = query.filter(Item.model.ilike(f'%{model}%'))
    if condition:
        query = query.filter(Item.overall_condition == condition)
    if assigned_to:
        query = query.join(Student, Item.current_student_id == Student.id).filter(
            (Student.first_name + ' ' + Student.last_name).ilike(f'%{assigned_to}%')
        )
    if type_filter:
        query = query.filter(Item.type == type_filter)

    items = query.all()
    total_items = len(items)
    conditions = ['New', 'Excellent', 'Very Good', 'Good', 'Damaged - Usable', 'Needs Repair', 'Damaged Beyond Repair', 'Retired', 'Lost/Stolen', 'Unknown']
    types = ['Chromebook', 'PowerAdapter', 'Bag']
    return render_template('index.html', items=items, total_items=total_items, conditions=conditions, types=types)

@item_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_type = request.form.get('item_type')
        quantity = int(request.form.get('quantity', 1))
        received_date = request.form.get('received_date') or datetime.now().date().isoformat()

        barcode_prefixes = {
            'Chromebook': 'USD349-CB-',
            'PowerAdapter': 'USD349-PWR-',
            'Bag': 'USD349-BAG-'
        }
        prefix = barcode_prefixes.get(item_type, 'USD349-')

        # Count existing items of the same type for numbering
        existing_count = Item.query.filter(Item.type == item_type).count()
        start_number = existing_count + 1

        for i in range(quantity):
            if item_type == 'Chromebook':
                item = Chromebook(
                    serial_number=request.form.get('serial_number'),
                    model=request.form.get('model'),
                    provisioned_date=request.form.get('provisioned_date') or datetime.now().date().isoformat(),
                    received_date=received_date,
                    overall_condition=request.form.get('overall_condition', 'Unknown'),
                    bezel_condition=request.form.get('bezel_condition', 'Unknown'),
                    hinge_cap=request.form.get('hinge_cap', 'Unknown'),
                    disposition=request.form.get('disposition', ''),
                    type='Chromebook'
                )
                refresh_date_option = request.form.get('refresh_date_option')
                if refresh_date_option == 'auto':
                    item.refresh_date = (datetime.now() + timedelta(days=5*365)).date().isoformat()
                else:
                    item.refresh_date = request.form.get('refresh_date') or (datetime.now() + timedelta(days=5*365)).date().isoformat()
            elif item_type == 'PowerAdapter':
                item = PowerAdapter(
                    serial_number=request.form.get('serial_number'),
                    model=request.form.get('model'),
                    received_date=received_date,
                    condition=request.form.get('condition', 'Unknown'),
                    type='PowerAdapter'
                )
            elif item_type == 'Bag':
                item = Bag(
                    received_date=received_date,
                    condition=request.form.get('condition', 'Unknown'),
                    type='Bag'
                )
            else:
                flash('Invalid item type.', 'error')
                return redirect(url_for('item.add_item'))

            # Generate barcode with type-specific number
            item.barcode = f'{prefix}{str(start_number + i).zfill(5)}'

            db.session.add(item)

        try:
            db.session.commit()
            flash(f'{quantity} item(s) added successfully!', 'success')
            return redirect(url_for('item.home'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding item: {str(e)}', 'error')
            return redirect(url_for('item.add_item'))

    # GET request
    barcode = ''
    barcode_prefixes = {
        'Chromebook': 'USD349-CB-',
        'PowerAdapter': 'USD349-PWR-',
        'Bag': 'USD349-BAG-'
    }
    item_type = request.args.get('item_type', 'Chromebook')
    prefix = barcode_prefixes.get(item_type, 'USD349-CB-')

    logger.debug(f"Generating barcode for item_type: {item_type}, prefix: {prefix}")
    existing_count = Item.query.filter(Item.type == item_type).count()
    next_number = existing_count + 1
    barcode = f'{prefix}{str(next_number).zfill(5)}'
    logger.debug(f"Generated barcode: {barcode}")

    conditions = ['New', 'Excellent', 'Very Good', 'Good', 'Damaged - Usable', 'Needs Repair', 'Damaged Beyond Repair', 'Retired', 'Lost/Stolen', 'Unknown']
    bezel_conditions = ['New', 'Good', 'Damaged - Usable', 'Broken', 'Missing', 'Unknown']
    hinge_conditions = ['New', 'Good', 'Damaged', 'Missing', 'Unknown']
    dispositions = ['For Parts', 'Disposed']
    return render_template('add_item.html', barcode=barcode, item_type=item_type,
                         conditions=conditions, bezel_conditions=bezel_conditions,
                         hinge_conditions=hinge_conditions, dispositions=dispositions)

@item_bp.route('/lookup')
def lookup():
    lookup_type = request.args.get('lookup_type')
    identifier = request.args.get('identifier')
    logger.debug(f"Lookup called with type: {lookup_type}, identifier: {identifier}")

    item = None
    if lookup_type == 'barcode':
        item = Item.query.filter_by(barcode=identifier).first()
    elif lookup_type == 'serial':
        item = Item.query.filter_by(serial_number=identifier).first()

    if item:
        assignments = Assignment.query.filter_by(chromebook_id=item.id).order_by(Assignment.checkout_date.desc()).all()
        logger.debug(f"Found item: {item.barcode}, assignments: {len(assignments)}")
        return render_template('item_detail.html', item=item, assignments=assignments)
    else:
        logger.warning(f"No item found for {lookup_type}: {identifier}")
        flash('Item not found.', 'error')
        return redirect(url_for('item.home'))

@item_bp.route('/checkout/<barcode>', methods=['GET', 'POST'])
def checkout(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        flash('Item not found.', 'error')
        return redirect(url_for('item.home'))

    if item.current_student_id:
        flash('Item is already checked out.', 'error')
        return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

    if request.method == 'POST':
        search_query = request.form.get('search_query', '').strip()
        grade_level = request.form.get('grade_level', '')

        students = Student.query
        if search_query:
            students = students.filter(
                (Student.first_name + ' ' + Student.last_name).ilike(f'%{search_query}%') |
                Student.student_id.ilike(f'%{search_query}%')
            )
        if grade_level:
            students = students.filter_by(grade_level=grade_level)

        students = students.all()
        return render_template('checkout.html', item=item, students=students, search_query=search_query, grade_level=grade_level)

    return render_template('checkout.html', item=item, students=None)

@item_bp.route('/checkout/<barcode>/confirm', methods=['POST'])
def checkout_confirm(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    student_id = request.form.get('student_id')
    student = Student.query.get(student_id)

    if not item or not student:
        flash('Invalid item or student.', 'error')
        return redirect(url_for('item.home'))

    item.current_student_id = student.id
    item.student_barcode = f"{2025 + (12 - student.grade_level)}-{student.student_id}"

    assignment = Assignment(
        chromebook_id=item.id,
        student_id=student.id,
        student_barcode=item.student_barcode,
        checkout_date=datetime.now().date(),
        grade_at_checkout=student.grade_level
    )
    db.session.add(assignment)
    db.session.commit()

    flash(f'Item checked out to {student.first_name} {student.last_name}.', 'success')
    return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

@item_bp.route('/checkin/<barcode>', methods=['POST'])
def checkin(barcode):
    item = Item.query.filter_by(barcode=barcode).first()
    if not item:
        flash('Item not found.', 'error')
        return redirect(url_for('item.home'))

    if not item.current_student_id:
        flash('Item is not checked out.', 'error')
        return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

    assignment = Assignment.query.filter_by(chromebook_id=item.id, checkin_date=None).first()
    if assignment:
        assignment.checkin_date = datetime.now().date()

    item.current_student_id = None
    item.student_barcode = None
    db.session.commit()

    flash('Item checked in successfully.', 'success')
    return redirect(url_for('item.lookup', lookup_type='barcode', identifier=barcode))

@item_bp.route('/upload_inventory', methods=['GET', 'POST'])
def upload_inventory():
    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('No file uploaded.', 'error')
            return redirect(url_for('item.upload_inventory'))

        try:
            stream = StringIO(file.stream.read().decode('UTF-8'), newline=None)
            csv_reader = csv.DictReader(stream)
            required_columns = ['barcode', 'serial_number', 'model', 'type', 'received_date']

            for row in csv_reader:
                if not all(col in row for col in required_columns):
                    flash('CSV missing required columns.', 'error')
                    return redirect(url_for('item.upload_inventory'))

                item_type = row['type']
                received_date = row.get('received_date') or datetime.now().date().isoformat()

                if item_type == 'Chromebook':
                    item = Chromebook(
                        barcode=row['barcode'],
                        serial_number=row['serial_number'],
                        model=row['model'],
                        type='Chromebook',
                        received_date=received_date,
                        overall_condition=row.get('overall_condition', 'Unknown'),
                        bezel_condition=row.get('bezel_condition', 'Unknown'),
                        hinge_cap=row.get('hinge_cap', 'Unknown'),
                        provisioned_date=row.get('provisioned_date', datetime.now().date().isoformat()),
                        refresh_date=row.get('refresh_date', (datetime.now() + timedelta(days=5*365)).date().isoformat()),
                        disposition=row.get('disposition', '')
                    )
                elif item_type == 'PowerAdapter':
                    item = PowerAdapter(
                        barcode=row['barcode'],
                        serial_number=row['serial_number'],
                        model=row['model'],
                        type='PowerAdapter',
                        received_date=received_date,
                        condition=row.get('condition', 'Unknown')
                    )
                elif item_type == 'Bag':
                    item = Bag(
                        barcode=row['barcode'],
                        type='Bag',
                        received_date=received_date,
                        condition=row.get('condition', 'Unknown')
                    )
                else:
                    flash(f'Invalid item type: {item_type}', 'error')
                    continue

                db.session.add(item)
                db.session.flush()

                student_identifier = row.get('student_name') or row.get('student_id')
                if student_identifier:
                    student = Student.query.filter(
                        (Student.first_name + ' ' + Student.last_name).ilike(f'%{student_identifier}%') |
                        Student.student_id == student_identifier
                    ).first()
                    if student:
                        item.current_student_id = student.id
                        item.student_barcode = f"{2025 + (12 - student.grade_level)}-{student.student_id}"
                        assignment = Assignment(
                            chromebook_id=item.id,
                            student_id=student.id,
                            student_barcode=item.student_barcode,
                            checkout_date=datetime.now().date(),
                            grade_at_checkout=student.grade_level
                        )
                        db.session.add(assignment)

            db.session.commit()
            flash('Inventory uploaded successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error uploading inventory: {str(e)}', 'error')

        return redirect(url_for('item.home'))

    return render_template('upload_inventory.html')

@item_bp.route('/export_inventory')
def export_inventory():
    items = Item.query.all()
    output = StringIO()
    writer = csv.writer(output)

    writer.writerow(['barcode', 'serial_number', 'model', 'type', 'received_date', 'condition', 'overall_condition', 'bezel_condition', 'hinge_cap', 'refresh_date', 'current_student'])

    for item in items:
        current_student = ''
        if item.current_student_id:
            student = Student.query.get(item.current_student_id)
            if student:
                current_student = f"{student.first_name} {student.last_name}"

        writer.writerow([
            item.barcode,
            item.serial_number,
            item.model,
            item.type,
            item.received_date,
            getattr(item, 'condition', ''),
            getattr(item, 'overall_condition', ''),
            getattr(item, 'bezel_condition', ''),
            getattr(item, 'hinge_cap', ''),
            getattr(item, 'refresh_date', ''),
            current_student
        ])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype='text/csv',
        headers={'Content-Disposition': 'attachment; filename=inventory.csv'}
    )

@item_bp.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    try:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting item: {str(e)}', 'error')

    return redirect(url_for('item.home'))