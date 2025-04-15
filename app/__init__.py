from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.system_info import SYSTEM_INFO

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.models.item import Item, Chromebook
    from app.models.student import Student
    from app.models.assignment import Assignment

    from app.routes.item_routes import item_bp
    from app.routes.student_routes import student_bp
    app.register_blueprint(item_bp, url_prefix='/items')
    app.register_blueprint(student_bp, url_prefix='/students')

    @app.route('/')
    def root():
        return redirect(url_for('item.home'))

    @app.route('/info')
    def system_info():
        return render_template('system_info.html', system_info=SYSTEM_INFO)

    return app