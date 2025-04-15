from app import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chromebook_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student_barcode = db.Column(db.String(20), nullable=False)
    checkout_date = db.Column(db.Date, nullable=False)
    checkin_date = db.Column(db.Date)
    grade_at_checkout = db.Column(db.String(20))
    
    # Relationship to Student model, added in Step 91, reapplied in Step 95
    student = db.relationship('Student', backref='assignments', lazy='select')