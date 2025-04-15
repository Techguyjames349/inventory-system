from app import db

class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(50), unique=True, nullable=False)
    serial_number = db.Column(db.String(50), unique=True, nullable=True)  # Made nullable for bags
    model = db.Column(db.String(100), nullable=True)  # Made nullable for bags
    type = db.Column(db.String(50), nullable=False)
    received_date = db.Column(db.Date)
    quantity = db.Column(db.Integer, default=1)
    current_student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student_barcode = db.Column(db.String(50))
    
    # Common condition field for all items
    condition = db.Column(db.String(50))
    
    # Chromebook-specific fields (nullable for non-Chromebook items)
    overall_condition = db.Column(db.String(50))
    bezel_condition = db.Column(db.String(50))
    hinge_cap = db.Column(db.String(50))
    provisioned_date = db.Column(db.Date)
    refresh_date = db.Column(db.Date)
    disposition = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'item'  # Base identity
    }

    def __repr__(self):
        return f"<Item {self.barcode}>"

class Chromebook(Item):
    __mapper_args__ = {'polymorphic_identity': 'chromebook'}

class PowerAdapter(Item):
    __mapper_args__ = {'polymorphic_identity': 'power_adapter'}

class Bag(Item):
    __mapper_args__ = {'polymorphic_identity': 'bag'}