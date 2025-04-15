from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    from app.routes.item_routes import item_bp
    from app.routes.student_routes import student_bp
    app.register_blueprint(item_bp)
    app.register_blueprint(student_bp)
    
    @app.route('/')
    def index():
        return redirect(url_for('item.items'))
    
    @app.route('/info')
    def system_info():
        # Combine prompt.md and history.md for display
        docs_dir = os.path.join(app.root_path, 'docs')
        prompt_file = os.path.join(docs_dir, 'prompt.md')
        history_file = os.path.join(docs_dir, 'history.md')
        content = []
        for file_path in [prompt_file, history_file]:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content.append(f.read())
            except Exception as e:
                content.append(f"Error reading {file_path}: {str(e)}")
        system_info_content = '\n\n'.join(content)
        return render_template('system_info.html', system_info=system_info_content)
    
    return app