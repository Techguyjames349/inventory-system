from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os
import glob

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
        # Read only prompt.md for display
        prompt_file = os.path.join(app.root_path, 'docs', 'prompt.md')
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                system_info_content = f.read()
        except Exception as e:
            system_info_content = f"Error reading {prompt_file}: {str(e)}"
        return render_template('system_info.html', system_info=system_info_content)

    return app