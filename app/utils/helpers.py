from datetime import datetime

GRADE_MAP = {
    'Sixth Grade': 6, 'Seventh Grade': 7, 'Eighth Grade': 8, 'Ninth Grade': 9,
    'Tenth Grade': 10, 'Eleventh Grade': 11, 'Twelfth Grade': 12,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
}

GRADE_REVERSE = {str(v): k for k, v in GRADE_MAP.items() if isinstance(k, str) and 'Grade' in k}

def get_graduation_year(grade_level):
    grade_num = GRADE_MAP.get(grade_level, 12)
    current_year = datetime.now().year
    return current_year + (12 - grade_num)

def generate_student_barcode(student):
    grad_year = get_graduation_year(student.grade_level)
    return f"{grad_year}-{student.student_id}"